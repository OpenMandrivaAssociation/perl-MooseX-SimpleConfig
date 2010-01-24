%define upstream_name    MooseX-SimpleConfig
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Moose role for setting attributes from a simple configfile
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::Any)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::ConfigFromFile)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


