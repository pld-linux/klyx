%define kdeprefix /usr
%define version 0.10.0
%define release 1
%define qtver  qt >= 1.42

%define kdename klyx
Name: %{kdename}
Summary: KLyX - a document processor for the K Desktop Environment
Version: %{version}
Release: %{release}
Source: ftp.kde.org:/pub/kde/unstable/apps/office/%{kdename}-%{version}.tar.gz
URL: http://www.devel.lyx.org/~ettrich/klyx.html
Group: Applications/Publishing
Copyright: GPL
Buildroot: /var/tmp/%{kdename}-buildroot
Requires: %{qtver} tetex kdesupport
Prefix: %{kdeprefix}
Vendor: The KLyX team (Matthias Ettrich, Kalle Dalheimer, and others)

%description
A document processor for the K Desktop Environment that is based
on LyX and uses LaTeX as its background formatting engine.

%description -l it
KLyX è un word processor per il KDE basato su LyX; utilizza LaTeX
come motore di formattazione.

%description -l de
Ein Dokumentenverarbeitungssystem für den KDE Desktop basierend auf LyX.
Verwendet LaTeX als Hintergrundsatzsystem.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n klyx-%{version}

%build
export KDEDIR=%{kdeprefix}
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{kdeprefix} --with-install-root=$RPM_BUILD_ROOT
make -j2 

%install
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
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version} $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}


%changelog
* Thu May 27 1999 Gerald Teschl <gerald@esi.ac.at>
- Updated
