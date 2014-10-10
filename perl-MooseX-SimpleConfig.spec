%define upstream_name    MooseX-SimpleConfig%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A Moose role for setting attributes from a simple configfile
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Test::Fatal)
BuildRequires:	perl(Config::Any)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::ConfigFromFile)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This role loads simple configfiles to set object attributes. It is based on
the abstract role the MooseX::ConfigFromFile manpage, and uses the
Config::Any manpage to load your configfile. the Config::Any manpage will
in turn support any of a variety of different config formats, detected by
the file extension. See the Config::Any manpage for more details about
supported formats.

Like all the MooseX::ConfigFromFile manpage -derived configfile loaders,
this module is automatically supported by the the MooseX::Getopt manpage
role as well, which allows specifying '-configfile' on the commandline.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 653603
- rebuild for updated spec-helper

  + Jérôme Quelin <jquelin@mandriva.org>
    - no need for this tarball

* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 570556
- update to 0.09

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 552422
- update to 0.07

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 536192
- update to 0.06

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 495431
- update to 0.05

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 466793
- import perl-MooseX-SimpleConfig


* Tue Nov 17 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

