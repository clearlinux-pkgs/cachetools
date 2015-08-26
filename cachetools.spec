#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cachetools
Version  : 1.1.1
Release  : 3
URL      : https://pypi.python.org/packages/source/c/cachetools/cachetools-1.1.1.tar.gz
Source0  : https://pypi.python.org/packages/source/c/cachetools/cachetools-1.1.1.tar.gz
Summary  : Extensible memoizing collections and decorators
Group    : Development/Tools
License  : MIT
Requires: cachetools-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
cachetools
========================================================================

%package python
Summary: python components for the cachetools package.
Group: Default

%description python
python components for the cachetools package.


%prep
%setup -q -n cachetools-1.1.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
