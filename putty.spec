%define		_snapshot	2003-08-31
%define		_snapver	%(echo %{_snapshot} | tr -d -)
Summary:	Remembers telnet and SSH sessions
Summary(pl):	Zapamiêtywanie sesji telnet i SSH
Name:		putty
Version:	0.53b
Release:	0.%{snapver}.0.1
License:	? Free ?
Group:		X11/Applications/Networking
Source0:	http://www.tartarus.org/~simon/putty-unix/%{name}-%{version}-%{_snapshot}.tar.gz
# Source0-md5:	4094754b959e1df5b90b9a14dd2c382a
URL:		http://www.tartarus.org/~simon/putty-unix/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


%prep
%setup -q -n %{name}-%{version}-%{_snapshot}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README README.txt
#%attr(755,root,root) %{_bindir}/gputty
