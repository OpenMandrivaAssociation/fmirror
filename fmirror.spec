Summary:	FTP mirroring package
Name:		fmirror
Version:	0.8.4
Release:	%mkrel 11
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

