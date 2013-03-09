Name:		kjumpingcube
Version:	4.10.1
Release:	1
Epoch:		1
Summary:	A tactical game for number-crunchers
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kjumpingcube
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KJumpingCube is a tactical one or two-player game. The playing field
consists of squares that contains points which can be increased. By
this you can gain more fields and finally win the board over.

%files
%{_kde_bindir}/kjumpingcube
%{_kde_applicationsdir}/kjumpingcube.desktop
%{_kde_appsdir}/kjumpingcube
%{_kde_datadir}/config.kcfg/kjumpingcube.kcfg
%{_kde_docdir}/*/*/kjumpingcube
%{_kde_iconsdir}/hicolor/*/apps/kjumpingcube.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

