%include	/usr/lib/rpm/macros.perl
Summary:	BnP perl module
Summary(pl):	Modu� perla BnP
Name:		perl-BnP
Version:	2.1.0
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module//BnP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Build'n'Play is a batch tool intended for system administrators who
have to install the same software packages (including, but not limited
to Perl) on various Unix platforms over and over again (e.g. for
perio- dically upgrading existing or installing new machines).

%description -l pl
Modu� perla Build'n'Play jest narz�dziem dla administartor�w
u�atwiaj�cym instalacj� tych samych program�w (w��cznie z pakietami
perla) na wielu r�nych platformach unixowych.

%prep
%setup -q -n BnP-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz build genopt *bnp *.diff* misc/{mgenopt,restart,tags}
%{perl_sitelib}/BnP.pm
%{_mandir}/man3/*
