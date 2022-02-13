%global modname webcolors
 
Summary:	A python module for working with HTML/CSS color definitions.
Name:		python-%{modname}
Version:	1.11.1
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://github.com/ubernostrum/%{modname}
Source0:	https://github.com/ubernostrum/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(sphinx-rtd-theme)

BuildArch:      noarch

%description
webcolors is a module python for working with HTML/CSS color definitions.

Support is included for normalizing and converting between the following
formats (RGB colorspace only; conversion to/from HSL can be handled by
the colorsys module in the Python standard library):

 -   Specification-defined color names
 -   Six-digit hexadecimal
 -   Three-digit hexadecimal
 -   Integer rgb() triplet
 -   Percentage rgb() triplet

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}*

#--------------------------------------------------------------------

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

# docs
make -C docs html
	
%install
%py3_install

%check	
# remove binaries
rm -fr %{buildroot}%{python3_sitelib}/__pycache__
