%define upstream_name	 Parse-Yapp
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	Fully reentrant perl OO LALR(1) parser creator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Parse::Yapp module enables to create Perl OO fully reentrant
LALR(1) parser modules (see the Yapp.pm pod pages for more details)
and has been designed to be functionally as close as possible to yacc,
but using the full power of Perl and open to enhancements.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
find -type f | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/Parse
