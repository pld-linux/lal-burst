Summary:	LAL routines for burst gravitational wave data analysis
Summary(pl.UTF-8):	Procedury LAL do analizy danych fal grawitacyjnych wybuchów
Name:		lal-burst
Version:	1.5.9
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://software.ligo.org/lscsoft/source/lalsuite/lalburst-%{version}.tar.xz
# Source0-md5:	7367e2396e161fd8c24eff74bedc0e4d
Patch0:		%{name}-env.patch
URL:		https://wiki.ligo.org/DASWG/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gsl-devel >= 1.13
BuildRequires:	lal-devel >= 6.18.0
BuildRequires:	lal-metaio-devel >= 1.3.1
BuildRequires:	lal-simulation-devel >= 1.7.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	python3-numpy-devel
BuildRequires:	swig >= 3.0.12
BuildRequires:	swig-python >= 2.0.12
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	lal >= 6.18.0
Requires:	lal-metaio >= 1.3.1
Requires:	lal-simulation >= 1.7.0
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
Requires:	lal-devel >= 6.18.0
Requires:	lal-metaio-devel >= 1.3.1
Requires:	lal-simulation-devel >= 1.7.0

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
Requires:	octave-lal >= 6.18.0

%description -n octave-lalburst
Octave interface for LAL Burst.

%description -n octave-lalburst -l pl.UTF-8
Interfejs Octave do biblioteki LAL Burst.

%package -n python3-lalburst
Summary:	Python bindings for LAL Burst
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Burst
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-lal >= 6.18.0
Requires:	python3-lalmetaio >= 1.3.1
Requires:	python3-lalsimulation >= 1.7.0
Requires:	python3-modules
Requires:	python3-matplotlib
Requires:	python3-numpy >= 1:1.7
Requires:	python3-scipy
#python-glue (glue.lilolw, glue.offsetvector)
#python-pylal

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
%attr(755,root,root) %{_bindir}/lalburst_version
%attr(755,root,root) %{_libdir}/liblalburst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalburst.so.6
/etc/shrc.d/lalburst-user-env.csh
/etc/shrc.d/lalburst-user-env.fish
/etc/shrc.d/lalburst-user-env.sh

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalburst.so
%{_includedir}/lal/EPSearch.h
%{_includedir}/lal/GenerateBurst.h
%{_includedir}/lal/LALBurst*.h
%{_includedir}/lal/LIGOLwXMLBurstRead.h*
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
