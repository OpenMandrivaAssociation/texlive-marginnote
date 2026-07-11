%global tl_name marginnote
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Notes in the margin, even where \marginpar fails
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/marginnote
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginnote.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the command \marginnote that may be used instead
of \marginpar at almost every place where \marginpar cannot be used,
e.g., inside floats, footnotes, or in frames made with the framed
package.

