%define name kanjipad
%define version 1.2.1
%define release %mkrel 8

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-8mdv2011.0
+ Revision: 619877
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-7mdv2010.0
+ Revision: 429659
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-6mdv2009.0
+ Revision: 247496
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.1-4mdv2008.1
+ Revision: 140850
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import kanjipad


* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.1-4mdk
- Fix redundant BuildRequires
- %%mkrel 

* Fri Jul 15 2005 Laurent MONTEL <lmontel@mandriva.com> 1.2.1-3mdk
- Fix build on x86_64

* Fri Nov 19 2004 Olivier Blin <blino@mandrake.org> 1.2.1-2mdk
- birthday rebuild

* Thu Apr  3 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.1-1mdk
- first mdk version (thx pterjan)
