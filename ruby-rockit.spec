#%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby O-o Compiler construction toolKIT
Summary(pl):	Zestaw narzêdzi do tworzenia i kompilowania kodu obiektowego w jêzyku Ruby
Name:		ruby-rockit
Version:	0.3.8
%define verstr 0-3-8
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/rockit/rockit-%{verstr}.tar.gz
# Source0-md5:	c09760f6bc47edb37e656f3179304a94
Patch0:	ruby-rockit-memoize-optional.patch
URL:		http://rockit.sourceforge.net/
BuildRequires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An easy-to-use, object-oriented compiler construction toolkit written
in and generating code for Ruby. Currently focusing on the "front-end"
phases of compiler construction.

%description -l pl
£atwy w u¿yciu zestaw narzêdzi do tworzenia i kompilowania kodu
obiektowego napisany i generuj±cy kod w jêzyku Ruby. Aktualnie skupia
siê na front-endowej czê¶ci tworzenia kompilatora.

%prep
%setup -q -n rockit-%{verstr}
%patch0 -p1

%build
cat > lib/version.rb <<EOF
def rockit_version
  "%{version}"
end
EOF

cd lib
for I in *.rb; do 
	BASE="$(echo $I | sed -e 's!.rb!!')"
	perl -pi -e "s#require '$BASE'#require 'rockit/$BASE'#" *.rb
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir}/rockit,%{_bindir}}

install lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}/rockit

echo '#!/usr/bin/ruby' > $RPM_BUILD_ROOT%{_bindir}/rockit
cat lib/rockit.rb >> $RPM_BUILD_ROOT%{_bindir}/rockit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples Changelog TODO docs
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/rockit
