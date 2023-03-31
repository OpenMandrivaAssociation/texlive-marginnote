Name:		texlive-marginnote
Version:	48383
Release:	2
Summary:	Notes in the margin, even where \marginpar fails
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/marginnote
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/marginnote
%doc %{_texmfdistdir}/doc/latex/marginnote
#- source
%doc %{_texmfdistdir}/source/latex/marginnote

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
