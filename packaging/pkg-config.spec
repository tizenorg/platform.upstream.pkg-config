Name:           pkg-config
Version:        0.27.1
Release:        0
Summary:        A library management system
License:        GPL-2.0+
Group:          System/Packages
Url:            http://pkgconfig.freedesktop.org/
Source:         http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
Provides:       pkgconfig = %{version}
Obsoletes:      pkgconfig < 0.21
# pkg-config has a virtual internal pkg-config.pc file, so we should provide it
Provides:       pkgconfig(pkg-config) = %{version}

%description
The pkg-config program is used to retrieve information about installed
libraries in the system. It is typically used to compile and link
against one or more libraries.

%prep
%setup -q

%build
%configure\
    --with-internal-glib \
%if "%{_lib}" == "lib"
       --with-pc_path=/usr/local/lib/pkgconfig:/usr/local/share/pkgconfig:%{_libdir}/pkgconfig:%{_datadir}/pkgconfig:/opt/kde3/%{_lib}/pkgconfig
%else
       --with-pc_path=/usr/local/%{_lib}/pkgconfig:/usr/local/lib/pkgconfig:/usr/local/share/pkgconfig:%{_libdir}/pkgconfig:%{_datadir}/pkgconfig:/opt/kde3/%{_lib}/pkgconfig
%endif
make %{?_smp_mflags}

%install
%make_install
# We'll put it with the other docs
rm %{buildroot}%{_datadir}/doc/pkg-config/pkg-config-guide.html

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/pkg-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/pkg.m4

%docs_package

%changelog
