# TODO:
# - prepare desktop
# - use .ico files that are included into .tar.gz
# - descriptions...
%define		snapshot	2003-08-31
%define		_snapver	%(echo %{snapshot} | tr -d -)
Summary:	Remembers telnet and SSH sessions
Summary(pl):	Zapamiêtywanie sesji telnet i SSH
Name:		putty
Version:	0.53b
Release:	0.%{_snapver}.1
License:	? Free ?
Group:		X11/Applications/Networking
Source0:	http://www.tartarus.org/~simon/putty-unix/%{name}-%{version}-%{snapshot}.tar.gz
# Source0-md5:	4094754b959e1df5b90b9a14dd2c382a
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.tartarus.org/~simon/putty-unix/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


%prep
%setup -q -n %{name}-%{version}-%{snapshot}
%patch0 -p1

%build
cd unix
%{__make} -f Makefile.gtk

# WARNING!!!
# this is REALLY temporary, because there are missing these manuals.
# Check if these are present in new version.
echo ".so putty.1" > pscp.1
echo ".so putty.1" > psftp.1

%install
rm -rf $RPM_BUILD_ROOT
cd unix
%{__make} -f Makefile.gtk install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=/usr \
	mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE MODULE README README.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
