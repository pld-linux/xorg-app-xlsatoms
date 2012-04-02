Summary:	xlsatoms application to list the interned atoms defined on an X11 server
Summary(pl.UTF-8):	Aplikacja xlsatoms do wypisywania elementów zdefiniowanych w serwerze X11
Name:		xorg-app-xlsatoms
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xlsatoms-%{version}.tar.bz2
# Source0-md5:	9d0e16d116d1c89e6b668c1b2672eb57
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xlsatoms application lists the interned atoms defined on an X11
server.

%description -l pl.UTF-8
Aplikacja xlsatoms wypisuje elementy (atomy) zdefiniowane wewnątrz
serwera X11.

%prep
%setup -q -n xlsatoms-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1x*
