# TODO
# - correct pl summary/descriptions
Summary:	Remembers telnet and SSH sessions
Summary(pl):	Zapamiêtywanie sesji telnet i SSH
Name:		putty
Version:	0.58
Release:	2
License:	MIT-licensed
Group:		X11/Applications/Networking
Source0:	http://the.earth.li/~sgtatham/putty/latest/%{name}-%{version}.tar.gz
# Source0-md5:	ffb78a7db7e4802896189b2112714a9f
Source1:	%{name}.desktop
Source2:	%{name}tel.desktop
Source3:	pterm.desktop
Source4:	%{name}.xpm
Source5:	%{name}cfg.xpm
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.tartarus.org/~simon/putty-unix/
Obsoletes:	%{name}-X11
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.

%description -l pl
PuTTY jest darmow± implementacj± telnetu i SSH dla platform Win32,
³±cznie z emulatorem terminala xterm, przeniesion± na platformê
uniksow±.

%package progs
Summary:	PuTTY additional programs
Summary(pl):	Zapamiêtywanie sesji telnet i SSH - program putty
Group:		X11/Applications/Networking

%description progs
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.

This package contains additional programs for PuTTY.

%description progs -l pl
PuTTY jest darmow± implementacj± telnetu i SSH dla platform Win32,
³±cznie z emulatorem terminala xterm, przeniesion± na platformê
uniksow±.

Ten pakiet zawiera additional program for PuTTY.

%package puttytel
Summary:	puttytel application
Summary(pl):	Zapamiêtywanie sesji telnet i SSH - program puttytel
Group:		X11/Applications/Networking

%description puttytel
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.

This package contains puttytel application.

%description puttytel -l pl
PuTTY jest darmow± implementacj± telnetu i SSH dla platform Win32,
³±cznie z emulatorem terminala xterm, przeniesion± na platformê
uniksow±.

Ten pakiet zawiera program puttytel.

%package pterm
Summary:	PuTTY terminal
Summary(pl):	Terminal PuTTY
Group:		Applications/Terminal

%description pterm
Pterm is terminal emulator from PuTTY package.

%description pterm -l pl
Pterm jest emulatorem terminala z pakietu PuTTY.

%prep
%setup -q
%patch0 -p1

%build
cd unix
%{__make} -f Makefile.gtk \
	CFLAGS="%{rpmcflags} `gtk-config --cflags` -I. -I.. -I../charset" \
	CC="%{__cc}"

# WARNING!!!
# this is REALLY temporary, because there are missing these manuals.
# Check if these are present in new version.
echo ".so putty.1" > pscp.1
echo ".so putty.1" > psftp.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
cd unix
%{__make} -f Makefile.gtk install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	mandir=%{_mandir}
cd ..
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/pterm.xpm
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}tel.xpm
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README README.txt
%attr(755,root,root) %{_bindir}/putty
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
%{_mandir}/man1/putty.1*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plink
%attr(755,root,root) %{_bindir}/pscp
%attr(755,root,root) %{_bindir}/psftp
%attr(755,root,root) %{_bindir}/puttygen
%{_mandir}/man1/plink.1*
%{_mandir}/man1/pscp.1*
%{_mandir}/man1/psftp.1*
%{_mandir}/man1/puttygen.1*

%files puttytel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}tel
%{_desktopdir}/%{name}tel.desktop
%{_pixmapsdir}/%{name}tel.xpm
%{_mandir}/man1/%{name}tel.1*

%files pterm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pterm
%{_desktopdir}/pterm.desktop
%{_pixmapsdir}/pterm.xpm
%{_mandir}/man1/pterm.1*
