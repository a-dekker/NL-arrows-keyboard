Name:       NL-arrows-keyboard

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    NL-arrows-keyboard
Version:    0.0.1
Release:    0
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qmake
Requires:   arrowboard-common

#Requires:   maliit-server

%description
Dutch  QWERTY virtual keyboard for SailfishOS

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_datadir}/maliit/plugins/com/jolla/*
%{_datadir}/maliit/plugins/com/jolla/layouts/*

%post
killall maliit-server
