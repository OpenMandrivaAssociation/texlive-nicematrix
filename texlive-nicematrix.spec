Name:		texlive-nicematrix
Version:	72084
Release:	1
Summary:	Improve the typesetting of mathematical matrices with PGF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nicematrix
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicematrix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicematrix.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicematrix.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is based on the package array. It creates PGF/TikZ
nodes under the cells of the array and uses these nodes to
provide functionalities to construct tabulars, arrays and
matrices. Among the features : continuous dotted lines for the
mathematical matrices; exterior rows and columns (so-called
border matrices); control of the width of the columns; tools to
color rows and columns with a good PDF result; blocks of cells;
etc. The package requires and loads l3keys2e, xparse, array,
amsmath, pgfcore, and the module shapes of PGF.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nicematrix
%{_texmfdistdir}/tex/latex/nicematrix
%doc %{_texmfdistdir}/doc/latex/nicematrix

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
