%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Summary:	Creates stand-alone executables from python scripts
Name:		python-bbfreeze
Version:	1.1.0
Release:	1%{?relprefix}%{?prerel}%{?dist}
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/bbfreeze/bbfreeze-%{version}.zip
URL:		http://pypi.python.org/pypi/bbfreeze
BuildRequires:	python-devel
BuildRequires:  python-setuptools
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbfreeze creates stand-alone executables from python scripts. It's
similar in purpose to the well known py2exe for windows, py2app for OS
X, PyInstaller and cx_Freeze (in fact ancient versions were based on
cx_Freeze. And it uses the modulegraph package, which is also used by
py2app).

%prep
%setup -q -n bbfreeze-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{python_sitelib}/*
%attr(755,root,root) %{_bindir}/bb-freeze
%attr(755,root,root) %{_bindir}/bbfreeze

%changelog
* Sat Apr 20 2013 David Johansen <david@makewhatis.com> - 1.1.0-1
- Refactoring spec file

