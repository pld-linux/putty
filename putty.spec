# TODO:
# - make separate packages with X and non-X applications

%define		snapshot	2003-08-31
%define		_snapver	%(echo %{snapshot} | tr -d -)
Summary:	Remembers telnet and SSH sessions
Summary(pl):	Zapamiêtywanie sesji telnet i SSH
Name:		putty
Version:	0.53b
Release:	0.%{_snapver}.2
License:	MIT-licensed
Group:		X11/Applications/Networking
Source0:	http://www.tartarus.org/~simon/putty-unix/%{name}-%{version}-%{snapshot}.tar.gz
# Source0-md5:	4094754b959e1df5b90b9a14dd2c382a
Source1:	%{name}.desktop
Source2:	%{name}tel.desktop
Source3:	pterm.desktop
Source4:	%{name}.xpm
Source5:	%{name}cfg.xpm
Source6:	%{name}gen.xpm
Source7:	scp.xpm
Source8:	pageant.xpm
Source9:	pageants.xpm
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
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE8} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE9} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE MODULE README README.txt
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Network/Communications/%{name}.desktop
%{_applnkdir}/Network/Communications/%{name}tel.desktop
%{_applnkdir}/Terminals/pterm.desktop
%{_mandir}/man1/*.1*
