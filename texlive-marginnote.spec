# revision 25880
# category Package
# catalog-ctan /macros/latex/contrib/marginnote
# catalog-date 2012-04-08 16:44:52 +0200
# catalog-license lppl
# catalog-version v1.1i
Name:		texlive-marginnote
Version:	v1.1i
Release:	3
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

%description
This package provides the command \marginnote that may be used
instead of \marginpar at almost every place where \marginpar
cannot be used, e.g., inside floats, footnotes, or in frames
made with the framed package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/marginnote/marginnote.sty
%doc %{_texmfdistdir}/doc/latex/marginnote/marginnote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/marginnote/README
%doc %{_texmfdistdir}/source/latex/marginnote/marginnote.dtx
%doc %{_texmfdistdir}/source/latex/marginnote/marginnote.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.1i-1
+ Revision: 790674
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.1f-2
+ Revision: 753766
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.1f-1
+ Revision: 718956
- texlive-marginnote
- texlive-marginnote
- texlive-marginnote
- texlive-marginnote

