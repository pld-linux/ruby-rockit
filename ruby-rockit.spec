#%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby O-o Compiler construction toolKIT
Name:		ruby-rockit
Version:	0.3.8
%define verstr 0-3-8
Release:	1
License:	LGPL
Source0:	http://dl.sourceforge.net/rockit/rockit-%{verstr}.tar.gz
# Source0-md5:	c09760f6bc47edb37e656f3179304a94
Group:		Development/Libraries
URL: http://rockit.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArchitectures: noarch
BuildRequires:	ruby

%description
An easy-to-use, object-oriented compiler construction toolkit written in and
generating code for Ruby. Currently focusing on the "front-end" phases of
compiler construction.

%prep
%setup -q -n rockit-%{verstr}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{ruby_rubylibdir}/rockit/
install -d $RPM_BUILD_ROOT/%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT/%{ruby_rubylibdir}/rockit/

echo '#!/usr/bin/ruby' > $RPM_BUILD_ROOT/%{_bindir}/rockit
cat lib/rockit.rb >> $RPM_BUILD_ROOT/%{_bindir}/rockit


%files
%defattr(644,root,root,755)
%doc README examples Changelog TODO docs
%{ruby_rubylibdir}/rockit
%attr(755,root,root) %{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT
