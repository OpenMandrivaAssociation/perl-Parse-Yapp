%define upstream_name	 Parse-Yapp
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Fully reentrant perl OO LALR(1) parser creator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Parse::Yapp module enables to create Perl OO fully reentrant
LALR(1) parser modules (see the Yapp.pm pod pages for more details)
and has been designed to be functionally as close as possible to yacc,
but using the full power of Perl and open to enhancements.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
find -type f | xargs chmod 644
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/Parse


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-5mdv2012.0
+ Revision: 765588
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-4
+ Revision: 764098
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-3
+ Revision: 667289
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 564826
- rebuild for perl 5.12.1

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 407957
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.05-10mdv2009.1
+ Revision: 351772
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.05-9mdv2009.0
+ Revision: 223952
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.05-8mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 1.05-8mdv2008.0
+ Revision: 19237
- rebuild


* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.05-7mdk
- Rebuild and cleanup

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.05-6mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05-5mdk
- rebuild for new auto{prov,req}

