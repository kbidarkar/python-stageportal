Name:		python-stageportal
Version:	0.2
Release:	1%{?dist}
Summary:	Python library and cli to work with stage portal

Group:		Development/Python
License:	GPLv3+
URL:		https://github.com/RedHatQE/python-stageportal
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

BuildRequires:	python-devel
Requires:	python-requests python-rhsm python-BeautifulSoup

%description
%summary

%prep
%setup -q

%build

%install
%{__python} setup.py install -O1 --root $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp bin/stageportal $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/stageportal.cfg
%{_bindir}/stageportal
%{python_sitelib}/stageportal/*.py*
%{python_sitelib}/*.egg-info

%changelog
* Wed Mar 19 2014 Vitaly Kuznetsov <vitty@redhat.com> 0.2-1
- new version (vitty@redhat.com)
* Tue Jul 30 2013 Vitaly Kuznetsov <vitty@redhat.com> 0.1-1
- new package built with tito


