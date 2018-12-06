# Run tests in check section
%bcond_without check

# https://github.com/golang/arch
%global goipath         golang.org/x/arch
%global forgeurl        https://github.com/golang/arch
%global commit          b19384d3c130858bb31a343ea8fce26be71b5998

%global common_description %{expand:
This package holds machine architecture information used by the Go
toolchain.}

%gometa 

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Machine architecture information used by the Go toolchain
# Detected licences
# - BSD 3-clause "New" or "Revised" License at 'LICENSE'
# BSD all except
# MIT x86/x86asm/testdata/libmach8db.c
# ASL 2.0 x86/x86avxgen/testdata/xedpath/*.txt
License:        BSD and MIT and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md PATENTS CONTRIBUTORS CONTRIBUTING.md AUTHORS


%changelog
* Mon Nov 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181126gitb19384d
- First package for Fedora

