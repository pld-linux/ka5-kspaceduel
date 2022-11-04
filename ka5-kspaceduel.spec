#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kspaceduel
Summary:	kspaceduel
Name:		ka5-%{kaname}
Version:	22.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1e6672cfae20e2bd066a64b4ecff12da
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In KSpaceDuel each of two possible players control a satellite
spaceship orbiting the sun. As the game progresses players have to
eliminate the opponent's spacecraft with bullets or mines.

%description -l pl.UTF-8
W KSpaceDuelu każdy z dwóch możliwych graczy kontroluje statek
kosmiczny orbitujący wokół słońca. W czasie trwania gry gracze
muszą eliminować statki rywala używając pocisków lub min.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspaceduel
%{_desktopdir}/org.kde.kspaceduel.desktop
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_iconsdir}/hicolor/128x128/apps/kspaceduel.png
%{_iconsdir}/hicolor/16x16/apps/kspaceduel.png
%{_iconsdir}/hicolor/22x22/apps/kspaceduel.png
%{_iconsdir}/hicolor/32x32/apps/kspaceduel.png
%{_iconsdir}/hicolor/48x48/apps/kspaceduel.png
%{_iconsdir}/hicolor/64x64/apps/kspaceduel.png
%{_datadir}/kspaceduel
%{_datadir}/metainfo/org.kde.kspaceduel.appdata.xml
