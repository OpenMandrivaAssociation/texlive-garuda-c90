Name:		texlive-garuda-c90
Version:	20111102
Release:	1
Summary:	TeX support (from CJK) for the garuda font in thailatex
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garuda-c90.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garuda-c90.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive garuda-c90 package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
