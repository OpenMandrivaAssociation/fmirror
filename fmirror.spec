Summary:	FTP mirroring package
Name:		fmirror
Version:	0.8.4
Release:	%mkrel 18
License:	GPLv2+
Group:		Networking/File transfer
URL:		ftp://ftp.sunet.se/pub/nir/ftp/utilities/fmirror/
Source:		ftp://ftp.sunet.se/pub/nir/ftp/utilities/fmirror/testing/%{name}-%{version}.tar.bz2
Patch0:		fmirror-mandriva.patch
Patch1:		fmirror-0.8.4-anonymous.patch
Patch2:		fmirror-0.8.4-typofix_inman.patch
Patch3:		fmirror-0.8.4-signal.patch
Patch4:		fmirror-0.8.4-skip-solaris-acl.patch
Patch5:		fmirror-0.8.4-maxdel.patch
Patch6:		fmirror-0.8.4-eol.patch
Patch7:		fmirror-0.8.4-remotez.patch
Patch8:		fmirror-0.8.4-bugfix.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is an FTP mirroring package; it is useful to keep in sync with some FTP
site.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/fmirror



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-15mdv2011.0
+ Revision: 664315
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-14mdv2011.0
+ Revision: 605170
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-13mdv2010.1
+ Revision: 522652
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.4-12mdv2010.0
+ Revision: 424457
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.8.4-11mdv2009.1
+ Revision: 364944
- use standard configure
- rediff maxdel patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4-10mdv2009.0
+ Revision: 220853
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4-9mdv2008.1
+ Revision: 149730
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/mandrake/mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.8.4-8mdv2008.0
+ Revision: 90205
- rebuild for 2008
- new license policy


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-7mdv2007.1
+ Revision: 145218
- Import fmirror

* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-7mdv2007.1
- use the %%mrel macro
- bunzip patches

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.4-6mdk
- build release

