Name: ab
Summary: ApacheBench standalone edition
URL: http://httpd.apache.org/
Vendor: Apache Software Foundation
License: Apache License, Version 2.0
Version: 2.4.25

Release: %(date +'%Y%m%d')%{?dist}
SOURCE: %{name}-%{version}.tar.gz
BuildRequires: gcc, openssl-devel, apr-devel >= 1.3.9, apr-util-devel >= 1.3.9

%define __os_install_post %{nil}
# %define debug_package %{nil}

%description
ApacheBench standalone - a Apache HTTP Server benchmark tool, known as ab.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install prefix=/usr

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc LICENSE NOTICE
%{_bindir}/ab
%{_mandir}/man1/ab.1*
