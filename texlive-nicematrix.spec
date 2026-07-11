%global tl_name nicematrix
%global tl_revision 79473

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.10a
Release:	%{tl_revision}.1
Summary:	Improve the typesetting of matrices and tabulars with PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nicematrix
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nicematrix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nicematrix.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nicematrix.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is based on the package array. It creates PGF/TikZ nodes
under the cells of the array and uses these nodes to provide
functionalities to construct tabulars, arrays and matrices. Among the
features : continuous dotted lines for the mathematical matrices;
exterior rows and columns (so-called border matrices); control of the
width of the columns; tools to color rows and columns with a good PDF
result; blocks of cells; tabular notes; etc. The package requires and
loads array, amsmath, pgfcore, and the module shapes of PGF.

