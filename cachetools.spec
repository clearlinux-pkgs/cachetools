#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cachetools
Version  : 4.1.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/30/62/88fda08df9053141647b6941141b71b4c2a23d0fabab485feb917428ab46/cachetools-4.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/62/88fda08df9053141647b6941141b71b4c2a23d0fabab485feb917428ab46/cachetools-4.1.0.tar.gz
Summary  : Extensible memoizing collections and decorators
Group    : Development/Tools
License  : MIT
Requires: cachetools-license = %{version}-%{release}
Requires: cachetools-python = %{version}-%{release}
Requires: cachetools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
========================================================================

%package license
Summary: license components for the cachetools package.
Group: Default

%description license
license components for the cachetools package.


%package python
Summary: python components for the cachetools package.
Group: Default
Requires: cachetools-python3 = %{version}-%{release}

%description python
python components for the cachetools package.


%package python3
Summary: python3 components for the cachetools package.
Group: Default
Requires: python3-core
Provides: pypi(cachetools)

%description python3
python3 components for the cachetools package.


%prep
%setup -q -n cachetools-4.1.0
cd %{_builddir}/cachetools-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588200682
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cachetools
cp %{_builddir}/cachetools-4.1.0/LICENSE %{buildroot}/usr/share/package-licenses/cachetools/032e9c18ee13324b4608033116bba3af670fe595
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cachetools/032e9c18ee13324b4608033116bba3af670fe595

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
