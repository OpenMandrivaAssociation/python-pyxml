%define module	PyXML

Summary:	XML libraries for python
Name:		python-pyxml
Version:	0.8.4
Release:	21
License:	MIT and Python and ZPLv1.0 and BSD
Group:		System/Libraries
Url:		http://pyxml.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyxml/%{module}-%{version}.tar.bz2
Patch0:		python-pyxml-fix_python_2.6.patch 
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(python)
Provides:	%{module} = %{version}-%{release}

%description
An XML package for Python. The distribution contains a validating XML parser,
an implementation of the SAX and DOM programming interfaces and an interface
to the Expat parser.

%prep
%setup -qn %{module}-%{version}
%patch0 -p0

%build
CFLAGS="%{optflags}" python setup.py build --with-libexpat=%{_prefix}

%install
python setup.py install -O 1 --root=%{buildroot} --record=INSTALLED_FILES 

%files
%doc LICENCE ANNOUNCE CREDITS README README.dom README.pyexpat README.sgmlop TODO doc/*
%{_bindir}/*
%{py_platsitedir}/PyXML-0.8.4-py2.7.egg-info
%{py_platsitedir}/_xmlplus/*py
%{py_platsitedir}/_xmlplus/marshal/
%{py_platsitedir}/_xmlplus/parsers/
%{py_platsitedir}/_xmlplus/sax/
%{py_platsitedir}/_xmlplus/schema/
%{py_platsitedir}/_xmlplus/unicode/
%{py_platsitedir}/_xmlplus/utils/
%{py_platsitedir}/_xmlplus/xpath/
%{py_platsitedir}/_xmlplus/dom/*py
%{py_platsitedir}/_xmlplus/dom/ext/
%{py_platsitedir}/_xmlplus/dom/html/
%lang(de) %{py_platsitedir}/_xmlplus/dom/de/
%lang(en_US) %{py_platsitedir}/_xmlplus/dom/en_US/
%lang(fr) %{py_platsitedir}/_xmlplus/dom/fr/

