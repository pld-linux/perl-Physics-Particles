#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Physics
%define	pnam	Particles
Summary:	Physics::Particles - Simulate particle dynamics
#Summary(pl):	
Name:		perl-Physics-Particles
Version:	1.01
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	466a845ca2efe0ffdbffa6673d2c3322
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Project3D
BuildRequires:	perl-Math-Project3D-Plot
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Physics::Particles is a facility to simulate movements of
a small number of particles under a small number of forces
that every particle excerts on the others. Complexity increases
with particles X particles X forces, so that is why the
number of particles should be low.

In the context of this module, a particle is no more or less
than a set of attributes like position, velocity, mass, and
charge. The example code and test cases that come with the
distribution simulate the inner solar system showing that
when your scale is large enough, planets and stars may
well be approximated as particles. (As a matter of fact,
in the case of gravity, if the planet's shape was a sphere,
the force of gravity outside the planet would always be
its mass times the mass of the body it excerts the force on
times the gravitational constant divided by the distance
squared.)

Simulation of microscopic particles is a bit more difficult
due to floating point arithmetics on extremely small values.
You will need to choose your constant factors wisely.



# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Physics/*.pm
#%{perl_vendorlib}/Physics/Particles
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
