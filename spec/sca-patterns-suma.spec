#
# spec file for package sca-patterns-suma
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define patmode 755
%define category suma

Name:           sca-patterns-suma
Version:        1.5.1
Release:        0
Summary:        Supportconfig Analysis Patterns for SUSE Manager
License:        GPL-2.0-only
URL:            https://github.com/g23guy/sca-patterns-suma
Group:          System/Monitoring
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
Requires:       sca-patterns-base >= 1.5.0
BuildArch:      noarch

%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SUSE Manager (SUMA)

See %{_docdir}/sca-patterns-base/COPYING.GPLv2

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}/%{patdir}/%{category}
install -d %{buildroot}/%{patdir}/%{category}/suma12all
install -d %{buildroot}/%{patdir}/%{category}/suma17all
install -d %{buildroot}/%{patdir}/%{category}/suma21all
install -m %{patmode} patterns/%{category}/suma12all/* %{buildroot}/%{patdir}/%{category}/suma12all
install -m %{patmode} patterns/%{category}/suma17all/* %{buildroot}/%{patdir}/%{category}/suma17all
install -m %{patmode} patterns/%{category}/suma21all/* %{buildroot}/%{patdir}/%{category}/suma21all
%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/suma12all
%dir %{patdir}/%{category}/suma17all
%dir %{patdir}/%{category}/suma21all
%attr(%{patmode},%{patuser},%{patgrp}) %{patdir}/%{category}/suma12all/*
%attr(%{patmode},%{patuser},%{patgrp}) %{patdir}/%{category}/suma17all/*
%attr(%{patmode},%{patuser},%{patgrp}) %{patdir}/%{category}/suma21all/*

%changelog
