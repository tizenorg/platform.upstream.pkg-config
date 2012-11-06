Name:           pkg-config
Version:        0.25
Release:        3
License:        GPL-2.0+
Summary:        A tool for determining compilation options
Url:            http://pkgconfig.freedesktop.org
Group:          Development/Tools
Source:         http://www.freedesktop.org/software/pkgconfig/releases/%{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  popt-devel

Provides:       pkgconfig(pkg-config) = %{version}
Provides:       pkgconfig

%description
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.

%prep
%setup -q

%build
cp %{SOURCE1001} .
%configure --disable-shared \
        --with-pc-path=%{_libdir}/pkgconfig:%{_datadir}/pkgconfig
make

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_datadir}/pkgconfig

# we include this below, already
rm -rf %{buildroot}%{_datadir}/doc/pkg-config

%remove_docs

%files
%manifest %{name}.manifest
%{_bindir}/*
%{_libdir}/pkgconfig
%{_datadir}/pkgconfig
%{_datadir}/aclocal/*
