# revision 16624
# category Package
# catalog-ctan /macros/latex/contrib/marginnote
# catalog-date 2010-01-07 11:41:23 +0100
# catalog-license lppl
# catalog-version v1.1f
Name:		texlive-marginnote
Version:	v1.1f
Release:	1
Summary:	Notes in the margin, even where \marginpar fails
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/marginnote
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides the command \marginnote that may be used
instead of \marginpar at almost every place where \marginpar
cannot be used, e.g., inside floats, footnotes, or in frames
made with the framed package.

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
%{_texmfdistdir}/tex/latex/marginnote/marginnote.sty
%doc %{_texmfdistdir}/doc/latex/marginnote/marginnote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/marginnote/README
%doc %{_texmfdistdir}/source/latex/marginnote/marginnote.dtx
%doc %{_texmfdistdir}/source/latex/marginnote/marginnote.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
