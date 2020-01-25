#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Physics
%define	pnam	Particles
Summary:	Physics::Particles - Simulate particle dynamics
Summary(pl.UTF-8):	Physics::Particles - symulacha dynamiki cząstek
Name:		perl-Physics-Particles
Version:	1.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Physics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c282ca4bc5f3ea4d36a0ddc421cd386f
URL:		http://search.cpan.org/dist/Physics-Particles/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Project3D
BuildRequires:	perl-Math-Project3D-Plot
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Physics::Particles is a facility to simulate movements of a small
number of particles under a small number of forces that every particle
excerts on the others. Complexity increases with particles X particles
X forces, so that is why the number of particles should be low.

In the context of this module, a particle is no more or less than a
set of attributes like position, velocity, mass, and charge. The
example code and test cases that come with the distribution simulate
the inner solar system showing that when your scale is large enough,
planets and stars may well be approximated as particles. (As a matter
of fact, in the case of gravity, if the planet's shape was a sphere,
the force of gravity outside the planet would always be its mass times
the mass of the body it excerts the force on times the gravitational
constant divided by the distance squared.)

Simulation of microscopic particles is a bit more difficult due to
floating point arithmetics on extremely small values. You will need to
choose your constant factors wisely.

%description -l pl.UTF-8
Physics::Particles to ułatwienie symulacji ruchu małej liczby cząstek
pod niewielką liczbą sił wywieranych przez każdą cząstkę na innych.
Złożoność wzrasta wraz z liczbą cząstek * liczbą cząstek * liczbą sił,
więc liczba cząstek powinna być mała.

W kontekście tego modułu cząstka jest ni mniej ni więcej tylko zbiorem
atrybutów takich jak położenie, prędkość, masa i ładunek. Kod
przykładowy i testy dostarczane z pakietem symulują wewnętrzny układ
słoneczny, pokazując, że przy wystarczająco dużej skali planety i
gwiazdy można dobrze aproksymować cząstkami (w istocie, w przypadku
grawitacji, gdyby planeta była sferą, siła grawitacji poza planetą
byłaby zawsze masą pomnożoną przez masę ciała w polu razy stała
grawitacyjna, podzieloną przez kwadrat odległości).

Symulacja cząstek mikroskopowych jest nieco trudna ze względu na
arytmetykę zmiennoprzecinkową na bardzo małych wartościach. Trzeba
mądrze dobierać współczynniki stałe.

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
%dir %{perl_vendorlib}/Physics
%{perl_vendorlib}/Physics/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
