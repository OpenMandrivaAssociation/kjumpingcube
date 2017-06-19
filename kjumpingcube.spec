%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kjumpingcube
Version:	17.04.2
Release:	1
Epoch:		1
Summary:	A tactical game for number-crunchers
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kjumpingcube
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
KJumpingCube is a tactical one or two-player game. The playing field
consists of squares that contains points which can be increased. By
this you can gain more fields and finally win the board over.

%files -f %{name}.lang
%{_bindir}/kjumpingcube
%{_datadir}/applications/org.kde.kjumpingcube.desktop
%{_datadir}/kjumpingcube
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_iconsdir}/hicolor/*/apps/kjumpingcube.png
%{_datadir}/kxmlgui5/kjumpingcube

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
