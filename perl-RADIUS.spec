#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	RADIUS
%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS - object-oriented Perl interface to RADIUS
Summary(pl.UTF-8):	RADIUS - obiektowy interfejs Perla do RADIUSa
Name:		perl-RADIUS
Version:	1.0
Release:	10
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RADIUS/RADIUS-%{version}.tar.gz
# Source0-md5:	c33fa63e6806d99c5b00507e9fcf63fa
Patch0:		%{name}-paths.patch
Patch1:		%{name}-Digest-MD5.patch
URL:		http://search.cpan.org/dist/RADIUS/
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS (RFC2138) specifies a binary packet format which contains
various values and attributes. This module provides an interface to
turn RADIUS packets into Perl data structures and vice-versa.

%description -l pl.UTF-8
RADIUS (RFC2138) definiuje binarny format pakietów, zawierający różne
wartości i atrybuty. Moduł ten udostępnia interfejs przekształcający
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
cp -p example*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *txt
%{perl_vendorlib}/RADIUS/Dictionary.pm
%{perl_vendorlib}/RADIUS/Packet.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
