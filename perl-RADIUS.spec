%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS perl module
Summary(pl):	Modu³ perla RADIUS
Name:		perl-RADIUS
Version:	1.0
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RADIUS/RADIUS-%{version}.tar.gz
# Source0-md5:	c33fa63e6806d99c5b00507e9fcf63fa
Patch0:		%{name}-paths.patch
Patch1:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
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
%{perl_vendorlib}/RADIUS/Dictionary.pm
%{perl_vendorlib}/RADIUS/Packet.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
