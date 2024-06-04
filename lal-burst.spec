Summary:	LAL routines for burst gravitational wave data analysis
Summary(pl.UTF-8):	Procedury LAL do analizy danych fal grawitacyjnych wybuchów
Name:		lal-burst
Version:	2.0.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalburst-%{version}.tar.xz
# Source0-md5:	5c61a04722478169daa1009bcebc6a9b
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/Computing/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gsl-devel >= 1.13
BuildRequires:	help2man >= 1.37
BuildRequires:	lal-devel >= 7.5.0
BuildRequires:	lal-metaio-devel >= 4.0.0
BuildRequires:	lal-simulation-devel >= 5.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel >= 1:1.7
BuildRequires:	swig >= 4.1.0
BuildRequires:	swig-python >= 3.0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gsl >= 1.13
Requires:	lal >= 7.5.0
Requires:	lal-metaio >= 4.0.0
Requires:	lal-simulation >= 5.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL routines for burst gravitational wave data analysis.

%description -l pl.UTF-8
Procedury LAL do analizy danych fal grawitacyjnych wybuchów.

%package devel
Summary:	Header files for lal-burst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lal-burst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gsl-devel >= 1.13
Requires:	lal-devel >= 7.5.0
Requires:	lal-metaio-devel >= 4.0.0
Requires:	lal-simulation-devel >= 5.4.0

%description devel
Header files for lal-burst library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lal-burst.

%package static
Summary:	Static lal-burst library
Summary(pl.UTF-8):	Statyczna biblioteka lal-burst
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-burst library.

%description static -l pl.UTF-8
Statyczna biblioteka lal-burst.

%package -n octave-lalburst
Summary:	Octave interface for LAL Burst
Summary(pl.UTF-8):	Interfejs Octave do biblioteki LAL Burst
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave-lal >= 7.5.0
Requires:	octave-lalmetaio >= 4.0.0
Requires:	octave-lalsimulation >= 5.4.0

%description -n octave-lalburst
Octave interface for LAL Burst.

%description -n octave-lalburst -l pl.UTF-8
Interfejs Octave do biblioteki LAL Burst.

%package -n python3-lalburst
Summary:	Python bindings for LAL Burst
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Burst
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-lal >= 7.5.0
Requires:	python3-lalmetaio >= 4.0.0
Requires:	python3-lalsimulation >= 5.4.0
Requires:	python3-ligo-lw >= 1.7.0
Requires:	python3-lscsoft-glue
Requires:	python3-matplotlib
Requires:	python3-modules >= 1:3.5
Requires:	python3-numpy >= 1:1.7
Requires:	python3-pillow
Requires:	python3-scipy
Obsoletes:	python-lalburst < 1.5.9

%description -n python3-lalburst
Python bindings for LAL Burst.

%description -n python3-lalburst -l pl.UTF-8
Wiązania Pythona do biblioteki LAL Burst.

%prep
%setup -q -n lalburst-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-swig
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblalburst.la

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/lalburst/cs_gamma.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/lalburst_*
%attr(755,root,root) %{_libdir}/liblalburst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalburst.so.8
/etc/shrc.d/lalburst-user-env.csh
/etc/shrc.d/lalburst-user-env.fish
/etc/shrc.d/lalburst-user-env.sh
%{_mandir}/man1/lalburst_*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalburst.so
%{_includedir}/lal/EPSearch.h
%{_includedir}/lal/GenerateBurst.h
%{_includedir}/lal/LALBurst*.h
%{_includedir}/lal/SWIGLALBurst*.h
%{_includedir}/lal/SWIGLALBurst*.i
%{_includedir}/lal/SnglBurstUtils.h
%{_includedir}/lal/cs_cosmo.h
%{_includedir}/lal/cs_lambda_cosmo.h
%{_includedir}/lal/swiglalburst.i
%{_pkgconfigdir}/lalburst.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblalburst.a

%files -n octave-lalburst
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/lalburst.oct

%files -n python3-lalburst
%defattr(644,root,root,755)
%dir %{py3_sitedir}/lalburst
%attr(755,root,root) %{py3_sitedir}/lalburst/_lalburst.so
%attr(755,root,root) %{py3_sitedir}/lalburst/cs_gamma.so
%{py3_sitedir}/lalburst/*.py
%{py3_sitedir}/lalburst/__pycache__
