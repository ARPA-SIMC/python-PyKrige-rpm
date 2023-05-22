%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-PyKrige
Version:        1.5.0
Release:        1%{?dist}
Summary:   Kriging Toolkit for Python.

License:        BSD 3-Clause
URL:            https://github.com/GeoStat-Framework/PyKrige
Source0:        https://files.pythonhosted.org/packages/source/P/PyKrige/PyKrige-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  %{python3_vers}-devel
BuildRequires:  %{python3_vers}-Cython
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(numpy) >= 1.14.5
BuildRequires:  python3dist(matplotlib)
%{!?el8:BuildRequires: python3dist(scikit-learn)}

%description
Kriging Toolkit for Python.

%package     -n %{python3_vers}-PyKrige
Summary:   Kriging Toolkit for Python.

%description -n %{python3_vers}-PyKrige
Kriging Toolkit for Python.

%prep
%autosetup -n PyKrige-%{version}

%build
%py3_build

%install
%py3_install

%check
# epel 8 is missing scikit-learn, needed for tests
%{!?el8:%{__python3} setup.py test}

%files -n %{python3_vers}-PyKrige
%{python3_sitearch}/*


%changelog
* Mon Jun 29 2020 Daniele Branchini <dbranchini@arpae.it> - 1.5.0-1
- Initial package
