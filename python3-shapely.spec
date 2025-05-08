# TODO: Package shapely/examples to _examplesdir ?
#
# Conditional build:
%bcond_with	tests	# unit tests

%define	module	shapely
Summary:	Geospatial geometries, predicates, and operations for Python
Summary(pl.UTF-8):	Geometrie, predykaty i operacje geoprzestrzenne dla Pythona
Name:		python3-%{module}
Version:	2.1.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/s/shapely/shapely-%{version}.tar.gz
# Source0-md5:	8798ffa7f67d1eaa4d4d158d34fe269a
URL:		https://pypi.org/project/Shapely
BuildRequires:	geos-devel >= 3.3
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-numpy-devel
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	geos >= 3.3
Requires:	python3-modules >= 1:3.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shapely is a Python package for manipulation and analysis of 2D
geospatial geometries. It is based on GEOS. Shapely is not concerned
with data formats or coordinate reference systems.

%description -l pl.UTF-8
Pakiet do operacji i analizy dwuwymiarowych geometrii
geoprzestrzennych. Jest oparty na GEOS, nie zajmuje się formatami
danych czy układami odniesienia współrzędnych.

%prep
%setup -q -n shapely-%{version}

%build
%py3_build

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt LICENSE.txt README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/*.py
%dir %{py3_sitedir}/%{module}/algorithms
%{py3_sitedir}/%{module}/algorithms/__pycache__
%{py3_sitedir}/%{module}/algorithms/*.py
%dir %{py3_sitedir}/%{module}/examples
%{py3_sitedir}/%{module}/examples/__pycache__
%{py3_sitedir}/%{module}/examples/*.py
%dir %{py3_sitedir}/%{module}/geometry
%{py3_sitedir}/%{module}/geometry/__pycache__
%{py3_sitedir}/%{module}/geometry/*.py
%dir %{py3_sitedir}/%{module}/speedups
%{py3_sitedir}/%{module}/speedups/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/speedups/*.so
%{py3_sitedir}/%{module}/speedups/*.py
%dir %{py3_sitedir}/%{module}/vectorized
%{py3_sitedir}/%{module}/vectorized/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/vectorized/*.so
%{py3_sitedir}/%{module}/vectorized/*.py
%{py3_sitedir}/Shapely-*.egg-info
