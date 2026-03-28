%global srcname python-pam
%global debug_package %{nil}

Name:           pam_python
Version:        1.0.8
Release:        4%{?dist}
Summary:        Python PAM authentication module

License:        MIT
URL:            https://github.com/jpegleg/python-pam
Source0:        https://github.com/jpegleg/python-pam/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
Simple Python bindings for PAM authentication. This provides a
drop-in replacement for the Python 2 pam_python package for use
with Howdy and other applications that require PAM authentication.

%prep
%autosetup -n %{srcname}-%{version}

%build
# Pure Python module, no compilation needed

%install
mkdir -p %{buildroot}%{python3_sitelib}
install -m 0644 pam.py %{buildroot}%{python3_sitelib}/

%check
%{python3} -c "import sys; sys.path.insert(0, '%{buildroot}%{python3_sitelib}'); import pam; print('OK')"

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/pam.py
%{python3_sitelib}/__pycache__/pam.cpython-314*

%changelog
* Sat Mar 28 2026 Marcus Oliveira - 1.0.8-4
- Rebuild for Fedora 43 with Python 3 support (drop Python 2.7 dependency)
