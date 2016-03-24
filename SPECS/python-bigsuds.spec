%{?el5:%define _without_egg_info 1}
%{?el6:%define _without_egg_info 1}
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define real_name bigsuds

Name: python-bigsuds
Version: 1.0.3
Release: 1
Summary: Python library for F5 Networks iControl API

Group: Development/Languages
License: https://devcentral.f5.com/resources/devcentral-eula
URL: http://devcentral.f5.com

BuildArch: noarch
BuildRequires: python-devel
Requires: python-suds >= 0.4

%prep

%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/%{real_name}/
%{!?_without_egg_info:%{python_sitelib}/*.egg-info}

%changelog
* Wed 24 2016 Roger Welin <roger.welin@icloud.com>
- First package of python-bigsuds
