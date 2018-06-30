#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httpretty
Version  : 0.8.14
Release  : 37
URL      : http://pypi.debian.net/httpretty/httpretty-0.8.14.tar.gz
Source0  : http://pypi.debian.net/httpretty/httpretty-0.8.14.tar.gz
Summary  : HTTP client mock for Python
Group    : Development/Tools
License  : MIT
Requires: httpretty-python3
Requires: httpretty-license
Requires: httpretty-python
BuildRequires : backports.ssl_match_hostname
BuildRequires : certifi-python
BuildRequires : coverage-python
BuildRequires : httplib2
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : sure-python
BuildRequires : tornado-python
BuildRequires : tox
BuildRequires : urllib3-python
BuildRequires : virtualenv
Patch1: test.patch

%description
===============

%package license
Summary: license components for the httpretty package.
Group: Default

%description license
license components for the httpretty package.


%package python
Summary: python components for the httpretty package.
Group: Default
Requires: httpretty-python3

%description python
python components for the httpretty package.


%package python3
Summary: python3 components for the httpretty package.
Group: Default
Requires: python3-core

%description python3
python3 components for the httpretty package.


%prep
%setup -q -n httpretty-0.8.14
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530327182
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/httpretty
cp COPYING %{buildroot}/usr/share/doc/httpretty/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/httpretty/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
