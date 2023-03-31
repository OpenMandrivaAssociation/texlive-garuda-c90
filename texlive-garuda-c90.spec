Name:		texlive-garuda-c90
Version:	60832
Release:	2
Summary:	TeX support (from CJK) for the garuda font
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garuda-c90.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garuda-c90.source.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts source %{buildroot}%{_texmfdistdir}
