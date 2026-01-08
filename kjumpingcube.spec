#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kjumpingcube
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
Summary:	A tactical game for number-crunchers
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://games.kde.org/game.php?game=kjumpingcube
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kjumpingcube/-/archive/%{gitbranch}/kjumpingcube-%{gitbranchd}.tar.bz2#/kjumpingcube-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kjumpingcube-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WidgetsAddons)

%rename plasma6-kjumpingcube

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KJumpingCube is a tactical one or two-player game. The playing field
consists of squares that contains points which can be increased. By
this you can gain more fields and finally win the board over.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kjumpingcube.categories
%{_datadir}/qlogging-categories6/kjumpingcube.renamecategories
%{_bindir}/kjumpingcube
%{_datadir}/applications/org.kde.kjumpingcube.desktop
%{_datadir}/kjumpingcube
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_datadir}/metainfo/org.kde.kjumpingcube.appdata.xml
%{_iconsdir}/hicolor/*/apps/kjumpingcube.png
