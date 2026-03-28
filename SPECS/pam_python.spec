%global srcname pam_python
%global debug_package %{nil}

Name:           python3-pam-python
Version:        0.1.44
Release:        1%{?dist}
Summary:        Python bindings for PAM (Pluggable Authentication Modules)

License:        GPL-2.0-or-later
URL:            https://github.com/heart/pam-python
Source0:        %{pypi_source %{srcname}}

BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  pyproject-rpm-macros

%description
python-pam provides Python bindings for PAM (Pluggable Authentication Modules).
It allows writing PAM modules in Python.

This package provides the Python 3 module.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pam_python

%check
%{python3} -c "import pam_python; print('pam_python import OK')"

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Mar 28 2026 Marcus Oliveira <marcuoli@gmail.com> - 0.1.44-1
- Initial Fedora 43 package for pam_python
