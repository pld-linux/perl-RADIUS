%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS perl module
Summary(pl):	Modu³ perla RADIUS
Name:		perl-RADIUS
Version:	1.0
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/RADIUS/RADIUS-%{version}.tar.gz
Patch:		perl-RADIUS-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Digest-MD5
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
RADIUS - interface to RADIUS.

%description -l pl
RADIUS - interfejs do RADIUSa.

%prep
%setup -q -n RADIUS-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install example*.pl $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/RADIUS
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,rfc2138.txt,rfc2139.txt}.gz

%{perl_sitelib}/RADIUS/Dictionary.pm
%{perl_sitelib}/RADIUS/Packet.pm
%{perl_sitearch}/auto/RADIUS/.packlist

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
