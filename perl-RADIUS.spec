%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS perl module
Summary(pl):	Modu³ perla RADIUS
Name:		perl-RADIUS
Version:	1.0
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/RADIUS/RADIUS-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS - interface to RADIUS.

%description -l pl
RADIUS - interfejs do RADIUSa.

%prep
%setup -q -n RADIUS-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install example*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *txt
%{perl_sitelib}/RADIUS/Dictionary.pm
%{perl_sitelib}/RADIUS/Packet.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
