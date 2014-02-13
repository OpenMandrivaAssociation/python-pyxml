%define module	PyXML
%define name	python-pyxml
%define version 0.8.4
%define release 20

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://pyxml.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyxml/%{module}-%{version}.tar.bz2
Patch0:		python-pyxml-fix_python_2.6.patch 
License:	MIT and Python and ZPLv1.0 and BSD
Group:		System/Libraries
Summary:	XML libraries for python
BuildRequires:	pkgconfig(expat)
Obsoletes:	%{module}
Provides:	%{module}
BuildRequires:  pkgconfig(python)

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
python setup.py install -O 1 --root=%{buildroot} --record=INSTALLED_FILES 

%files
%defattr(-,root,root)
%doc LICENCE ANNOUNCE CREDITS README README.dom README.pyexpat README.sgmlop TODO doc/*
%_bindir/*
%py_platsitedir/PyXML-0.8.4-py2.7.egg-info
%py_platsitedir/_xmlplus/*py
%py_platsitedir/_xmlplus/marshal/
%py_platsitedir/_xmlplus/parsers/
%py_platsitedir/_xmlplus/sax/
%py_platsitedir/_xmlplus/schema/
%py_platsitedir/_xmlplus/unicode/
%py_platsitedir/_xmlplus/utils/
%py_platsitedir/_xmlplus/xpath/
%py_platsitedir/_xmlplus/dom/*py
%py_platsitedir/_xmlplus/dom/ext/
%py_platsitedir/_xmlplus/dom/html/
%lang(de) %{py_platsitedir}/_xmlplus/dom/de/
%lang(en_US) %{py_platsitedir}/_xmlplus/dom/en_US/
%lang(fr) %{py_platsitedir}/_xmlplus/dom/fr/

%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-16mdv2011.0
+ Revision: 668030
- mass rebuild

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.8.4-15mdv2011.0
+ Revision: 589988
- rebuild for python 2.7

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild for python-2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-13mdv2010.1
+ Revision: 523855
- rebuilt for 2010.1

* Mon Jan 12 2009 Michael Scherer <misc@mandriva.org> 0.8.4-12mdv2009.1
+ Revision: 328796
- fix usage with python 2.6, patch from p. Christeas, on bug 46709

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild with python 2.6
    - correct license (from Fedora, thanks)

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.8.4-11mdv2009.1
+ Revision: 318985
- rebuild for new python

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4-10mdv2009.0
+ Revision: 225139
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.8.4-9mdv2008.1
+ Revision: 136460
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 13 2007 Michael Scherer <misc@mandriva.org> 0.8.4-9mdv2008.0
+ Revision: 85024
- fix bug 32835 ( missing .pyo in pacakges )

* Thu Jun 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.4-8mdv2008.0
+ Revision: 36932
- rebuild for expat


* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.4-7mdv2007.0
+ Revision: 88167
- Import python-pyxml

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.8.4-7mdv2007.1
- update file list

* Wed Feb 01 2006 Michael Scherer <misc@mandriva.org> 0.8.4-6mdk
- really fix file listing for amd64

* Mon Jan 30 2006 Michael Scherer <misc@mandriva.org> 0.8.4-5mdk
- fix file listing, and no longer ship .pyo

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.8.4-4mdk
- depend on python

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8.4-3mdk
- Rebuild

* Thu May 05 2005 Götz Waschk <waschk@mandriva.org> 0.8.4-2mdk
- use external libexpat
- enable xpath and xslt

* Thu Dec 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.8.4-1mdk
- new version
- changed name

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.8.3-4mdk
- Rebuild for new python

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.8.3-3mdk
- [DIRM]

* Sun Apr 11 2004 Michael Scherer <misc@mandrake.org> 0.8.3-2mdk 
- [DIRM]

