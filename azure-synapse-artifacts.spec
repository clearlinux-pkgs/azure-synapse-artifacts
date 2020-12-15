#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-synapse-artifacts
Version  : 0.4.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/aa/ad/8a236277704dcd1ead333ce3db61e35e12a44214af803ee37816a4dd890b/azure-synapse-artifacts-0.4.0.zip
Source0  : https://files.pythonhosted.org/packages/aa/ad/8a236277704dcd1ead333ce3db61e35e12a44214af803ee37816a4dd890b/azure-synapse-artifacts-0.4.0.zip
Summary  : Microsoft Azure Synapse Artifacts Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-synapse-artifacts-python = %{version}-%{release}
Requires: azure-synapse-artifacts-python3 = %{version}-%{release}
Requires: azure-common
Requires: azure-core
Requires: msrest
BuildRequires : azure-common
BuildRequires : azure-core
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
This is the Microsoft Azure Synapse Artifacts Client Library.
        This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.

%package python
Summary: python components for the azure-synapse-artifacts package.
Group: Default
Requires: azure-synapse-artifacts-python3 = %{version}-%{release}

%description python
python components for the azure-synapse-artifacts package.


%package python3
Summary: python3 components for the azure-synapse-artifacts package.
Group: Default
Requires: python3-core
Provides: pypi(azure_synapse_artifacts)
Requires: pypi(azure_common)
Requires: pypi(azure_core)
Requires: pypi(msrest)

%description python3
python3 components for the azure-synapse-artifacts package.


%prep
%setup -q -n azure-synapse-artifacts-0.4.0
cd %{_builddir}/azure-synapse-artifacts-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608002641
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
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
