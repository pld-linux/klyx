Summary:	KLyX - a document processor for the K Desktop Environment
Summary(pl):	KLyX - procesor dokumentów dla KDE
Name:		klyx
Version:	0.10.0
Release:	3
License:	GPL
Group:		X11/KDE/Applications
Group(de):	X11/KDE/Applikationen
Group(pl):	X11/KDE/Aplikacje
Source:		ftp://ftp.kde.org/pub/kde/unstable/apps/office/%{name}-%{version}.tar.gz
URL:		http://www.devel.lyx.org/~ettrich/klyx.html
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel >= 1.42
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A document processor for the K Desktop Environment that is based
on LyX and uses LaTeX as its background formatting engine.

%description -l pl
Procesor dokumentów dla KDE bazuj±cy na LyXie, a u¿ywaj±cy LaTeXa 
w tle jako narzêdzia formatuj±cego.

%description -l it
KLyX è un word processor per il KDE basato su LyX; utilizza LaTeX
come motore di formattazione.

%description -l de
Ein Dokumentenverarbeitungssystem für den KDE Desktop basierend auf LyX.
Verwendet LaTeX als Hintergrundsatzsystem.

%prep
%setup -q

%build
KDEDIR=%{_prefix} ; export KDEDIR
CFLAGS="%{rpmcflags} -Wall" \
CXXFLAGS="%{rpmcflags} -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTIR=$RPM_BUILD_ROOT

gzip -9nf ANNOUNCE* CHANGES ChangeLog* PROBLEMS README* NEWS ToDo

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {CHANGES,ChangeLog*,PROBLEMS,README*,ANNOUNCE*,NEWS,ToDo}.gz
%attr(755,root,root) %{_bindir}/klyx

%dir %{_datadir}/kde/apps/klyx
%attr(755,root,root) %{_datadir}/kde/apps/klyx/configure
%{_datadir}/kde/apps/klyx/chkconfig.ltx
%{_datadir}/kde/apps/klyx/*.lst
%{_datadir}/kde/apps/klyx/lyxrc*
%{_datadir}/kde/apps/klyx/bind
%{_datadir}/kde/apps/klyx/clipart
%{_datadir}/kde/apps/klyx/doc
%{_datadir}/kde/apps/klyx/examples
%{_datadir}/kde/apps/klyx/kbd
%{_datadir}/kde/apps/klyx/layouts
%{_datadir}/kde/apps/klyx/pics
%{_datadir}/kde/apps/klyx/templates
%{_datadir}/kde/apps/klyx/tex
%{_datadir}/kde/icons/*.xpm
%{_datadir}/kde/icons/*.gif
%{_datadir}/kde/icons/mini/*.xpm

/etc/X11/kde/applnk/Applications/klyx.kdelnk
