Name:		texlive-pst-ovl
Version:	54963
Release:	2
Summary:	Create and manage graphical overlays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ovl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ovl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ovl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is useful when building an image from assorted
material, as in the slides of a projected presentation. The
package requires pstricks, and shares that package's
restrictions on usage when generating PDF output.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-ovl/pst-ovl.pro
%{_texmfdistdir}/tex/generic/pst-ovl/pst-ovl.tex
%{_texmfdistdir}/tex/latex/pst-ovl/pst-ovl.sty
%doc %{_texmfdistdir}/doc/generic/pst-ovl/Changes
%doc %{_texmfdistdir}/doc/generic/pst-ovl/README
%doc %{_texmfdistdir}/doc/generic/pst-ovl/pst-ovl-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-ovl/pst-ovl-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-ovl/pst-ovl-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
