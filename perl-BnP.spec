%include	/usr/lib/rpm/macros.perl
Summary:	BnP - implements the automatic recovery mechanism of "Build'n'Play"
Summary(pl.UTF-8):	BnP - implementacja automatycznego mechanizmu odzyskiwania dla "Build'n'Play"
Name:		perl-BnP
Version:	2.1.0
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/BnP/BnP-%{version}.tar.gz
# Source0-md5:	63eace514b995de9ad10f54b75eb2311
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Build'n'Play is a batch tool intended for system administrators who
have to install the same software packages (including, but not limited
to Perl) on various UNIX platforms over and over again (e.g. for
perio- dically upgrading existing or installing new machines).

%description -l pl.UTF-8
Moduł Perla Build'n'Play jest narzędziem dla administartorów
ułatwiającym instalację tych samych programów (włącznie z pakietami
Perla) na wielu różnych platformach uniksowych.

%prep
%setup -q -n BnP-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt genopt *bnp *.diff.linux misc/{mgenopt,restart,tags}
%{perl_vendorlib}/BnP.pm
%{_mandir}/man3/*
