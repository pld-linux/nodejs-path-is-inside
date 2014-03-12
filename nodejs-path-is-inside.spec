%define		pkg	path-is-inside
Summary:	Tests whether one path is inside another path
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	WTFPL
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	71ae8531120cccc208eac6f5e2eeae61
URL:		https://github.com/domenic/path-is-inside
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The path-is-inside package will give you a robust, cross-platform way
of detecting whether a given path is inside another path.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
