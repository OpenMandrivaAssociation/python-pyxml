%define module	PyXML
%define name	python-pyxml
%define version 0.8.4
%define release %mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://%{name}.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/pyxml/PyXML-%{version}.tar.bz2
License:	Apacheish License
Group:		System/Libraries
Summary:	XML libraries for python
BuildRequires:	python-devel
BuildRequires:	libexpat-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes:	%{module}
Provides:	%{module}
#gw we need full python
Requires:	python

%description
An XML package for Python. The distribution contains a validating XML parser,
an implementation of the SAX and DOM programming interfaces and an interface
to the Expat parser.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build --with-libexpat=%_prefix

%install
rm -fr $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc LICENCE ANNOUNCE CREDITS README README.dom README.pyexpat README.sgmlop TODO doc/*
%py_platsitedir/*
%_bindir/*
%lang(de) %{py_platsitedir}/*/dom/de/
%lang(en_US) %{py_platsitedir}/*/dom/en_US/
%lang(fr) %{py_platsitedir}/*/dom/fr/


