%include	/usr/lib/rpm/macros.perl
Summary:	BnP perl module
Summary(pl):	Modu³ perla BnP
Name:		perl-BnP
Version:	2.1.0
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module//BnP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/BnP
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        *txt *pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {genopt.txt,README.txt,*pod}.gz build genopt *bnp *.diff*
%doc misc/{mgenopt,restart,tags}

%{perl_sitelib}/BnP.pm
%{perl_sitearch}/auto/BnP

%{_mandir}/man3/*
