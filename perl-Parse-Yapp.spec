%define modname Parse-Yapp
%define modver 1.21

Summary:	Fully reentrant perl OO LALR(1) parser creator
Name:		perl-%{modname}
Version:	%{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Parse-Yapp
Source0:	https://cpan.metacpan.org/authors/id/W/WB/WBRASWELL/Parse-Yapp-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
The Parse::Yapp module enables to create Perl OO fully reentrant
LALR(1) parser modules (see the Yapp.pm pod pages for more details)
and has been designed to be functionally as close as possible to yacc,
but using the full power of Perl and open to enhancements.

%prep
%setup -qn %{modname}-%{modver}
find -type f | xargs chmod 644

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/*
%{perl_vendorlib}/Parse
%{_mandir}/man1/*
%{_mandir}/man3/*

