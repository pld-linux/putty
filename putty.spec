Summary:	Remembers telnet and SSH sessions
Summary(pl.UTF-8):	Zapamiętywanie sesji telnet i SSH
Name:		putty
Version:	0.73
Release:	1
License:	MIT-licensed
Group:		X11/Applications/Networking
Source0:	http://the.earth.li/~sgtatham/putty/latest/%{name}-%{version}.tar.gz
# Source0-md5:	d4a1797763e11e6a77115d0d0368b566
Source1:	%{name}.desktop
Source2:	%{name}tel.desktop
Source3:	pterm.desktop
URL:		http://www.chiark.greenend.org.uk/~sgtatham/putty/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	xorg-lib-libX11-devel
Obsoletes:	putty-X11
Obsoletes:	putty-pterm
Obsoletes:	putty-puttytel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.

%description -l pl.UTF-8
PuTTY jest darmową implementacją telnetu i SSH dla platform Win32,
łącznie z emulatorem terminala xterm, przeniesioną na platformę
uniksową.

%package progs
Summary:	PuTTY additional programs
Summary(pl.UTF-8):	Dodatkowe programy dla PuTTY
Group:		X11/Applications/Networking

%description progs
PuTTY is a free implementation of telnet and SSH for Win32 platforms,
along with an xterm terminal emulator, ported into Unix platform.

This package contains additional programs for PuTTY.

%description progs -l pl.UTF-8
PuTTY jest darmową implementacją telnetu i SSH dla platform Win32,
łącznie z emulatorem terminala xterm, przeniesioną na platformę
uniksową.

Ten pakiet zawiera dodatkowe programy dla PuTTY.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

cd icons
for size  in 16 32 48 64 96 128 ; do
	dir=hicolor/${size}x${size}/apps
	install -d $dir
	./mkicon.py -T putty_icon ${size} $dir/putty.png
	./mkicon.py -T pterm_icon ${size} $dir/pterm.png
done

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_desktopdir}}
cp -a icons/hicolor $RPM_BUILD_ROOT%{_iconsdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc LICENCE README
%attr(755,root,root) %{_bindir}/pterm
%attr(755,root,root) %{_bindir}/putty
%attr(755,root,root) %{_bindir}/puttytel
%{_mandir}/man1/pterm.1*
%{_mandir}/man1/putty.1*
%{_mandir}/man1/puttytel.1*
%{_desktopdir}/pterm.desktop
%{_desktopdir}/putty.desktop
%{_desktopdir}/puttytel.desktop
%{_iconsdir}/hicolor/*/apps/pterm.png
%{_iconsdir}/hicolor/*/apps/putty.png

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pageant
%attr(755,root,root) %{_bindir}/plink
%attr(755,root,root) %{_bindir}/pscp
%attr(755,root,root) %{_bindir}/psftp
%attr(755,root,root) %{_bindir}/puttygen
%{_mandir}/man1/pageant.1*
%{_mandir}/man1/plink.1*
%{_mandir}/man1/pscp.1*
%{_mandir}/man1/psftp.1*
%{_mandir}/man1/puttygen.1*
