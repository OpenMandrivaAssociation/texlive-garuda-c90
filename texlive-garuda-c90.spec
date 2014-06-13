# revision 30642
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-garuda-c90
Version:	20131012
Release:	6
Summary:	TeX support (from CJK) for the garuda font
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garuda-c90.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garuda-c90.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-fonts-tlwg

%description
TeXLive garuda-c90 package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/garuda-c90/config.garuda-c90
%{_texmfdistdir}/fonts/map/dvips/garuda-c90/garuda-c90.map
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdb8z.tfm
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdbo8z.tfm
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdo8z.tfm
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdr8z.tfm
#- source
%doc %{_texmfdistdir}/source/fonts/garuda-c90/garuda-c90.fontinst

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts source %{buildroot}%{_texmfdistdir}
