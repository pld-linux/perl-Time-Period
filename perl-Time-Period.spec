%include	/usr/lib/rpm/macros.perl
Summary:	Time::Period perl module
Summary(pl):	Modu³ perla Time::Period
Name:		perl-Time-Period
Version:	1.20
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/Period-%{version}.tar.gz
# Source0-md5:	63b073af8ec96e7fa48801cd6fcccdd1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Time::Period - A Perl module to deal with time periods.

%description -l pl
Time::Period - modu³ perla do operowania na okresach czasowych.

%prep
%setup -q -n Period-%{version}

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
%doc README
%{perl_vendorlib}/Time/Period.pm
%{_mandir}/man3/*
