Summary:	FTP mirroring package
Name:		fmirror
Version:	0.8.4
Release:	29
License:	GPLv2+
Group:		Networking/File transfer
Url:		ftp://ftp.sunet.se/pub/nir/ftp/utilities/fmirror/
Source0:	ftp://ftp.sunet.se/pub/nir/ftp/utilities/fmirror/testing/%{name}-%{version}.tar.bz2
Patch0:		fmirror-mandriva.patch
Patch1:		fmirror-0.8.4-anonymous.patch
Patch2:		fmirror-0.8.4-typofix_inman.patch
Patch3:		fmirror-0.8.4-signal.patch
Patch4:		fmirror-0.8.4-skip-solaris-acl.patch
Patch5:		fmirror-0.8.4-maxdel.patch
Patch6:		fmirror-0.8.4-eol.patch
Patch7:		fmirror-0.8.4-remotez.patch
Patch8:		fmirror-0.8.4-bugfix.patch

%description
This is an FTP mirroring package; it is useful to keep in sync with some FTP
site.

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/fmirror

