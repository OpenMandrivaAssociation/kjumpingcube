Name:		kjumpingcube
Version:	15.12.0
Release:	2
Epoch:		1
Summary:	A tactical game for number-crunchers
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kjumpingcube
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DocTools)

%description
KJumpingCube is a tactical one or two-player game. The playing field
consists of squares that contains points which can be increased. By
this you can gain more fields and finally win the board over.

%files
%{_bindir}/kjumpingcube
%{_datadir}/applications/org.kde.kjumpingcube.desktop
%{_datadir}/kjumpingcube
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_iconsdir}/hicolor/*/apps/kjumpingcube.png
%{_datadir}/kxmlgui5/kjumpingcube
%doc %{_docdir}/*/*/kjumpingcube

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
