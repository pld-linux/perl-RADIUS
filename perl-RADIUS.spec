#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS - object-oriented Perl interface to RADIUS
Summary(pl):	RADIUS - obiektowy interfejs Perla do RADIUSa
Name:		perl-RADIUS
Version:	1.0
Release:	8
License:	unknown
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
RADIUS (RFC2138) specifies a binary packet format which contains
various values and attributes.  This module provides an interface to
turn RADIUS packets into Perl data structures and vice-versa.

%description -l pl
RADIUS (RFC2138) definiuje binarny format pakiet�w, zawieraj�cy r�ne
warto�ci i atrybuty. Modu� ten udost�pnia interfejs przekszta�caj�cy
pakiety RADIUSa w struktury Perla i odwrotnie.

%prep
%setup -q -n RADIUS-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
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
