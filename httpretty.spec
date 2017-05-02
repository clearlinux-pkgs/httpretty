#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httpretty
Version  : 0.8.14
Release  : 23
URL      : http://pypi.debian.net/httpretty/httpretty-0.8.14.tar.gz
Source0  : http://pypi.debian.net/httpretty/httpretty-0.8.14.tar.gz
Summary  : HTTP client mock for Python
Group    : Development/Tools
License  : MIT
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
BuildRequires : python-dev
BuildRequires : python-mock
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
HTTPretty 0.8.3
===============
|https://s3-us-west-2.amazonaws.com/s.cdpn.io/18885/httpretty-logo_1.svg|
|tip for next commit| |Build Status| `ChangeLog <NEWS.md>`__

%package python
Summary: python components for the httpretty package.
Group: Default

%description python
python components for the httpretty package.


%prep
%setup -q -n httpretty-0.8.14
%patch1 -p1

%build
export LANG=C
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
