# spec file for package sca-patterns-suma
#
# Copyright (C) 2014 SUSE LLC
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Source developed at:
#  https://github.com/g23guy/sca-patterns-suma
#
# norootforbuild
# neededforbuild

%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define mode 544
%define category suma

Name:         sca-patterns-suma
Summary:      Supportconfig Analysis Patterns for SUSE Manager
URL:          https://github.com/g23guy/sca-patterns-suma
Group:        System/Monitoring
License:      GPL-2.0
Autoreqprov:  on
Version:      1.0
Release:      0
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
BuildRequires: fdupes
Requires:     sca-patterns-base

%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SUSE Manager (SUMA)

Authors:
--------
    Jason Record <jrecord@suse.com>

%prep
%setup -q

%build

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/suma21all
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/suma17all
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{sca_common}
install -m 444 patterns/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{sca_common}
install -m %{mode} patterns/%{category}/suma21all/* $RPM_BUILD_ROOT/%{patdir}/%{category}/suma21all
install -m %{mode} patterns/%{category}/suma17all/* $RPM_BUILD_ROOT/%{patdir}/%{category}/suma17all
%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/suma21all
%dir %{patdir}/%{category}/suma17all
%dir /usr/share/doc/packages/%{sca_common}
%doc %attr(-,root,root) /usr/share/doc/packages/%{sca_common}/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/suma21all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/suma17all/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

