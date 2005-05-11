#%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby O-o Compiler construction toolKIT
Summary(pl):	Zestaw narzêdzi do tworzenia i kompilowania kodu obiektowego w jêzyku Ruby
Name:		ruby-rockit
Version:	0.4.0
%define cvs 20041122
Release:	0.%{cvs}.1
License:	LGPL
Group:		Development/Libraries
Source0:	rockit-%{version}-%{cvs}.tar.gz
# Source0-md5:	432242f6a2627530ffab052cc495d19b
Source1:	setup.rb
Patch0:	rockit-class.patch
URL:		http://rockit.sourceforge.net/
BuildRequires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An easy-to-use, object-oriented compiler construction toolkit written
in and generating code for Ruby. Currently focusing on the "front-end"
phases of compiler construction.

%description -l pl
£atwy w u¿yciu zestaw narzêdzi do tworzenia i kompilowania kodu
obiektowego napisany i generuj±cy kod w jêzyku Ruby. Aktualnie skupia
siê na frontendowej czê¶ci tworzenia kompilatora.

%prep
%setup -q -n rockit
%patch0 -p1

%build
cp %{SOURCE1} .
#cat > lib/version.rb <<EOF
#def rockit_version
#  "%{version}"
#end
#EOF

cd lib
for I in *.rb; do
	BASE="$(echo $I | sed -e 's!.rb!!')"
	perl -pi -e "s#require '$BASE'#require 'rockit/$BASE'#" *.rb
done
cd -

mkdir bin
mkdir tmplib/rockit -p
cp lib/rockit.rb bin/rockit
mv lib/* tmplib/rockit
mv tmplib/* lib/

ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir}
ruby setup.rb setup

rdoc -o rdoc lib --inline-source
rdoc --ri lib -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples Changelog TODO docs
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/rockit
%{ruby_ridir}/AmbigousParseException
%{ruby_ridir}/AmbiguityNode
%{ruby_ridir}/ArrayNode
%{ruby_ridir}/ArrayNodeBuilder
%{ruby_ridir}/ArrayOfArrays
%{ruby_ridir}/ArrayOfHashes
%{ruby_ridir}/BackLinkedDirectedGraph
%{ruby_ridir}/BooleanMatrix
%{ruby_ridir}/BoundedLruCache
%{ruby_ridir}/ComplexTest
%{ruby_ridir}/DagPropagator
%{ruby_ridir}/DefaultInitArray
%{ruby_ridir}/DefaultInitHash
%{ruby_ridir}/DirectedGraph
%{ruby_ridir}/DotGraph
%{ruby_ridir}/DotGraphFormatter
%{ruby_ridir}/DotGraphPrinter
%{ruby_ridir}/Element
%{ruby_ridir}/EofToken
%{ruby_ridir}/EpsilonToken
%{ruby_ridir}/ForkingRegexpLexer
%{ruby_ridir}/GeneralizedLrParser
%{ruby_ridir}/Grammar
%{ruby_ridir}/GrammarSymbol
%{ruby_ridir}/GraphLink
%{ruby_ridir}/GraphTraversalException
%{ruby_ridir}/GroupingSyntaxTreeBuilder
%{ruby_ridir}/HashOfHash
%{ruby_ridir}/IndexableFactory
%{ruby_ridir}/Item
%{ruby_ridir}/LexerPosition
%{ruby_ridir}/LexerToken
%{ruby_ridir}/LiftingSyntaxTreeBuilder
%{ruby_ridir}/ListElement
%{ruby_ridir}/LrState
%{ruby_ridir}/MaybeElement
%{ruby_ridir}/MultElement
%{ruby_ridir}/NonTerminal
%{ruby_ridir}/OperatorElement
%{ruby_ridir}/OrElement
%{ruby_ridir}/Parse
%{ruby_ridir}/Parse/RockitProductionsEvaluator
%{ruby_ridir}/Parse/StateGraph
%{ruby_ridir}/ParseException
%{ruby_ridir}/ParseStack
%{ruby_ridir}/ParseTable
%{ruby_ridir}/PlusElement
%{ruby_ridir}/Production
%{ruby_ridir}/ProductionPriorities
%{ruby_ridir}/ReduceActionsGenerator
%{ruby_ridir}/ReferencingRegexpLexer
%{ruby_ridir}/RegexpToken
%{ruby_ridir}/Relation
%{ruby_ridir}/RelationCircularityException
%{ruby_ridir}/Rockit
%{ruby_ridir}/SourceCodeDumpable
%{ruby_ridir}/StackPath
%{ruby_ridir}/SyntaxTree
%{ruby_ridir}/SyntaxTreeAsDotGraph
%{ruby_ridir}/SyntaxTreeBuilder
%{ruby_ridir}/TerminalSet
%{ruby_ridir}/Token
%{ruby_ridir}/TokenRegexp
