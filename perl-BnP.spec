%include	/usr/lib/rpm/macros.perl
Summary:	BnP perl module
Summary(pl):	Modu³ perla BnP
Name:		perl-BnP
Version:	2.1.0
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/BnP/BnP-%{version}.tar.gz
# Source0-md5:	63eace514b995de9ad10f54b75eb2311
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Build'n'Play is a batch tool intended for system administrators who
have to install the same software packages (including, but not limited
to Perl) on various Unix platforms over and over again (e.g. for
perio- dically upgrading existing or installing new machines).

%description -l pl
Modu³ perla Build'n'Play jest narzêdziem dla administartorów
u³atwiaj±cym instalacjê tych samych programów (w³±cznie z pakietami
perla) na wielu ró¿nych platformach unixowych.

%prep
%setup -q -n BnP-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt genopt *bnp *.diff.linux misc/{mgenopt,restart,tags}
%{perl_vendorlib}/BnP.pm
%{_mandir}/man3/*
