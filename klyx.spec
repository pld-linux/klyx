Summary:	KLyX - a document processor for the K Desktop Environment
Summary(pl):	KLyX - procesor dokumentów dla KDE
Name:		klyx
Version:	0.10.0
Release:	1
Copyright:	GPL
Group:		Applications/Publishing
Vendor:		The KLyX team (Matthias Ettrich, Kalle Dalheimer, and others)
Source:		ftp://ftp.kde.org:/pub/kde/unstable/apps/office/%{name}-%{version}.tar.gz
URL:		http://www.devel.lyx.org/~ettrich/klyx.html
BuildRequires:	qt-devel >= 1.42
BuildRequires:	tetex
BuildRequires:	kdesupport-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
A document processor for the K Desktop Environment that is based
on LyX and uses LaTeX as its background formatting engine.

%description -l pl
Procesor dokumentów dla KDE bazuj±cy LyXa, a u¿ywaj±cy LaTeXa w tle
jako narzêdzia formatuj±cego.

%description -l it
KLyX è un word processor per il KDE basato su LyX; utilizza LaTeX
come motore di formattazione.

%description -l de
Ein Dokumentenverarbeitungssystem für den KDE Desktop basierend auf LyX.
Verwendet LaTeX als Hintergrundsatzsystem.

%prep
%setup -q

%build
export KDEDIR=%{kdeprefix}
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{kdeprefix} --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{kdeprefix}
make install-strip

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
        $RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
        -e '/\/config\//s|^|%config|' \
        -e '/\/applnk\//s|^|%config|' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
        $RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{kdename}
