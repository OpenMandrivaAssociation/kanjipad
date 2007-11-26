%define name kanjipad
%define version 1.2.1
%define release %mkrel 4

Name: %{name}
Summary: Japanese handwriting recognition
Version: %{version}
Release: %{release}
License: GPL
Group: System/Internationalization
URL: http://www.gtk.org/~otaylor/kanjipad/index.html
Source: ftp://ftp.gtk.org/pub/users/otaylor/kanjipad/%{name}-%{version}.tar.bz2
Patch0: kanjipad-1.2.1-add-useful-keyboard-shortcuts.patch.bz2
BuildRequires: gtk+1.2-devel
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KanjiPad is a simple (but snazzy) program which does Japanese handwriting
recognition. It uses the GTK toolkit for a GUI and Todd David Rudicks's
algorithms from JavaDict for recognition.

%prep
%setup -q
%patch0 -p0

%build
make BINDIR=%{_bindir} LIBDIR=%{_datadir}/%{name} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install BINDIR=$RPM_BUILD_ROOT%{_bindir} LIBDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_datadir}/*

