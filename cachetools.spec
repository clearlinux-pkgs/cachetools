#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cachetools
Version  : 4.0.0
Release  : 37
URL      : https://files.pythonhosted.org/packages/ff/e9/879bc23137b5c19f93c2133a6063874b83c8e1912ff1467a3d4331598921/cachetools-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/e9/879bc23137b5c19f93c2133a6063874b83c8e1912ff1467a3d4331598921/cachetools-4.0.0.tar.gz
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
cachetools
========================================================================

.. image:: http://img.shields.io/pypi/v/cachetools
   :target: https://pypi.org/project/cachetools/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/readthedocs/cachetools
   :target: http://cachetools.readthedocs.io/
   :alt: Documentation build status

.. image:: http://img.shields.io/travis/tkem/cachetools
   :target: https://travis-ci.org/tkem/cachetools/
   :alt: Travis CI build status

.. image:: http://img.shields.io/coveralls/tkem/cachetools
   :target: https://coveralls.io/r/tkem/cachetools
   :alt: Test coverage

.. image:: https://img.shields.io/github/license/tkem/cachetools
   :target: http://raw.github.com/tkem/cachetools/master/LICENSE
   :alt: License

This module provides various memoizing collections and decorators,
including variants of the Python Standard Library's `@lru_cache`_
function decorator.

.. code-block:: python

   from cachetools import cached, LRUCache, TTLCache

   # speed up calculating Fibonacci numbers with dynamic programming
   @cached(cache={})
   def fib(n):
       return n if n < 2 else fib(n - 1) + fib(n - 2)

   # cache least recently used Python Enhancement Proposals
   @cached(cache=LRUCache(maxsize=32))
   def get_pep(num):
       url = 'http://www.python.org/dev/peps/pep-%04d/' % num
       with urllib.request.urlopen(url) as s:
           return s.read()

   # cache weather data for no longer than ten minutes
   @cached(cache=TTLCache(maxsize=1024, ttl=600))
   def get_weather(place):
       return owm.weather_at_place(place).get_weather()

For the purpose of this module, a *cache* is a mutable_ mapping_ of a
fixed maximum size.  When the cache is full, i.e. by adding another
item the cache would exceed its maximum size, the cache must choose
which item(s) to discard based on a suitable `cache algorithm`_.  In
general, a cache's size is the total size of its items, and an item's
size is a property or function of its value, e.g. the result of
``sys.getsizeof(value)``.  For the trivial but common case that each
item counts as ``1``, a cache's size is equal to the number of its
items, or ``len(cache)``.

Multiple cache classes based on different caching algorithms are
implemented, and decorators for easily memoizing function and method
calls are provided, too.


Installation
------------------------------------------------------------------------

cachetools is available from PyPI_ and can be installed by running::

  pip install cachetools


Project Resources
------------------------------------------------------------------------

- `Documentation`_
- `Issue tracker`_
- `Source code`_
- `Change log`_


License
------------------------------------------------------------------------

Copyright (c) 2014-2019 Thomas Kemmer.

Licensed under the `MIT License`_.


.. _@lru_cache: http://docs.python.org/3/library/functools.html#functools.lru_cache
.. _mutable: http://docs.python.org/dev/glossary.html#term-mutable
.. _mapping: http://docs.python.org/dev/glossary.html#term-mapping
.. _cache algorithm: http://en.wikipedia.org/wiki/Cache_algorithms

.. _PyPI: https://pypi.org/project/cachetools/
.. _Documentation: https://cachetools.readthedocs.io/
.. _Issue tracker: https://github.com/tkem/cachetools/issues/
.. _Source code: https://github.com/tkem/cachetools/
.. _Change log: https://github.com/tkem/cachetools/blob/master/CHANGELOG.rst
.. _MIT License: http://raw.github.com/tkem/cachetools/master/LICENSE

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
%setup -q -n cachetools-4.0.0
cd %{_builddir}/cachetools-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582903437
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cachetools
cp %{_builddir}/cachetools-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/cachetools/66ea0242dc7ab9bd36eb130b98ae0c7117b034a7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cachetools/66ea0242dc7ab9bd36eb130b98ae0c7117b034a7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
