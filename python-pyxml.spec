%define module	PyXML

Summary:	XML libraries for python
Name:		python-pyxml
Version:	0.8.4
Release:	26
License:	MIT and Python and ZPLv1.0 and BSD
Group:		System/Libraries
Url:		https://pyxml.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyxml/%{module}-%{version}.tar.bz2
Patch0:		python-pyxml-fix_python_2.6.patch 
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(python2)
Provides:	%{module} = %{version}-%{release}

%description
An XML package for Python. The distribution contains a validating XML parser,
an implementation of the SAX and DOM programming interfaces and an interface
to the Expat parser.

%prep
%setup -qn %{module}-%{version}
%patch0 -p0

%build
CFLAGS="%{optflags}" python2 setup.py build --with-libexpat=%{_prefix}

%install
python2 setup.py install -O 1 --root=%{buildroot} --record=INSTALLED_FILES 

find %{buildroot} -name *.pyo -exec rm -f {} \;
find %{buildroot} -name *.pyc -exec rm -f {} \;

%files
%doc LICENCE ANNOUNCE CREDITS README README.dom README.pyexpat README.sgmlop TODO doc/*
%{_bindir}/*
%{py2_platsitedir}/PyXML-0.8.4-py2.7.egg-info
%{py2_platsitedir}/_xmlplus/*py
%{py2_platsitedir}/_xmlplus/marshal/
%{py2_platsitedir}/_xmlplus/parsers/
%{py2_platsitedir}/_xmlplus/sax/
%{py2_platsitedir}/_xmlplus/schema/
%{py2_platsitedir}/_xmlplus/unicode/
%{py2_platsitedir}/_xmlplus/utils/
%{py2_platsitedir}/_xmlplus/xpath/
%{py2_platsitedir}/_xmlplus/dom/*py
%{py2_platsitedir}/_xmlplus/dom/ext/
%{py2_platsitedir}/_xmlplus/dom/html/
%lang(de) %{py2_platsitedir}/_xmlplus/dom/de/
%lang(en_US) %{py2_platsitedir}/_xmlplus/dom/en_US/
%lang(fr) %{py2_platsitedir}/_xmlplus/dom/fr/

