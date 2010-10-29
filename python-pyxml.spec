%define module	PyXML
%define name	python-pyxml
%define version 0.8.4
%define release %mkrel 15

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://pyxml.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyxml/%{module}-%{version}.tar.bz2
Patch0:		python-pyxml-fix_python_2.6.patch 
License:	MIT and Python and ZPLv1.0 and BSD
Group:		System/Libraries
Summary:	XML libraries for python
BuildRequires:	libexpat-devel >= 2.0.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes:	%{module}
Provides:	%{module}
%py_requires -d

%description
An XML package for Python. The distribution contains a validating XML parser,
an implementation of the SAX and DOM programming interfaces and an interface
to the Expat parser.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
CFLAGS="%{optflags}" python setup.py build --with-libexpat=%{_prefix}

%install
rm -fr %{buildroot}
python setup.py install -O 1 --root=%{buildroot} --record=INSTALLED_FILES 

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc LICENCE ANNOUNCE CREDITS README README.dom README.pyexpat README.sgmlop TODO doc/*
%py_platsitedir/*
%_bindir/*
%lang(de) %{py_platsitedir}/*/dom/de/
%lang(en_US) %{py_platsitedir}/*/dom/en_US/
%lang(fr) %{py_platsitedir}/*/dom/fr/
