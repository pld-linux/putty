%define		snapshot	2004-02-12
%define		_snapver	%(echo %{snapshot} | tr -d -)
Summary:	Remembers telnet and SSH sessions
Summary(pl):	Zapamiêtywanie sesji telnet i SSH
Name:		putty
Version:	0.54
Release:	0.%{_snapver}.1
License:	MIT-licensed
Group:		X11/Applications/Networking
Source0:	http://www.tartarus.org/~simon/putty-unix/%{name}-%{version}-%{snapshot}.tar.gz
# Source0-md5:	6cc21b0ee5909a679433bec8b48fa37d
Source1:	%{name}.desktop
Source2:	%{name}tel.desktop
Source3:	pterm.desktop
Source4:	%{name}.xpm
Source5:	%{name}cfg.xpm
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.tartarus.org/~simon/putty-unix/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.

%description -l pl
PuTTY jest darmow± implementacj± telnetu i SSH dla platform Win32,
³±cznie z emulatorem terminala xterm, przeniesion± na platformê
uniksow±.

%package X11
Summary:	Remembers telnet and SSH sessions - putty application
Summary(pl):	Zapamiêtywanie sesji telnet i SSH - program putty
Group:		X11/Appplications/Networking

%description X11
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.
This package contains only putty X11 application.

%description X11 -l pl
PuTTY jest darmow± implementacj± telnetu i SSH dla platform Win32,
³±cznie z emulatorem terminala xterm, przeniesion± na platformê
uniksow±.
Ten pakiet zawiera tylko program putty dla X11.

%package puttytel
Summary:	Remembers telnet and SSH sessions - puttytel application
Summary(pl):	Zapamiêtywanie sesji telnet i SSH - program puttytel
Group:		X11/Appplications/Networking

%description puttytel
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.
This package contains only puttytel X11 application.

%description puttytel -l pl
PuTTY jest darmow± implementacj± telnetu i SSH dla platform Win32,
³±cznie z emulatorem terminala xterm, przeniesion± na platformê
uniksow±.
Ten pakiet zawiera tylko program puttytel dla X11.

%package pterm
Summary:	PuTTY terminal
Summary(pl):	Terminal PuTTY
Group:		Applications/Terminal

%description pterm
Pterm is terminal emulator from PuTTY package.

%description pterm -l pl
Pterm jest emulatorem terminala z pakietu PuTTY.

%prep
%setup -q -n %{name}-%{version}-%{snapshot}
%patch0 -p1

%build
cd unix
%{__make} -f Makefile.gtk \
	CFLAGS="%{rpmcflags} `gtk-config --cflags` -I. -I.. -I../charset" \
	CC=%{__cc}

# WARNING!!!
# this is REALLY temporary, because there are missing these manuals.
# Check if these are present in new version.
echo ".so putty.1" > pscp.1
echo ".so putty.1" > psftp.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/{Network/Communications,Terminals}}
cd unix
%{__make} -f Makefile.gtk install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	mandir=%{_mandir}
cd ..
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Terminals
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/pterm.xpm
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}tel.xpm
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE MODULE README README.txt
%attr(755,root,root) %{_bindir}/plink
%attr(755,root,root) %{_bindir}/pscp
%attr(755,root,root) %{_bindir}/psftp
%attr(755,root,root) %{_bindir}/puttygen
%{_mandir}/man1/plink.1*
%{_mandir}/man1/pscp.1*
%{_mandir}/man1/psftp.1*
%{_mandir}/man1/puttygen.1*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/putty
%{_applnkdir}/Network/Communications/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_mandir}/man1/putty.1*

%files puttytel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}tel
%{_applnkdir}/Network/Communications/%{name}tel.desktop
%{_pixmapsdir}/%{name}tel.xpm
%{_mandir}/man1/%{name}tel.1*

%files pterm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pterm
%{_applnkdir}/Terminals/pterm.desktop
%{_pixmapsdir}/pterm.xpm
%{_mandir}/man1/pterm.1*
