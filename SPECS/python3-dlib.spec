%global srcname dlib
%global debug_package %{nil}

Name:           python3-dlib
Version:        19.24.6
Release:        1%{?dist}
Summary:        Toolkit for machine learning and computer vision

License:        BSL-1.0
URL:            https://github.com/davisking/dlib
Source0:        %{pypi_source %{srcname}}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
dlib is a modern C++ toolkit containing machine learning algorithms and tools for
creating complex software in C++ to solve real world problems.

This package provides the Python 3 module.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -n %{srcname}-%{version}

%build
# Disable optional GUI code to keep server/headless builds reliable.
export DLIB_NO_GUI_SUPPORT=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dlib

%check
%{python3} -c "import dlib; print('dlib import OK')"

%files -f %{pyproject_files}
%{python3_sitearch}/_dlib_pybind11*.so
%license dlib/LICENSE.txt
%doc README.md

%changelog
* Sat Mar 28 2026 Copilot <copilot@example.com> - 19.24.6-1
- Initial Fedora package
