Summary:	Windows CE remote control tool like VNC
Summary(pl.UTF-8):	Narzędzie do sterowania Windows CE podobne do VNC
Summary(ru.UTF-8):	Управление Windows CE в стиле VNC
Summary(uk.UTF-8):	Керування Windows CE у стилі VNC
Name:		synce-gcemirror
Version:	0.4
Release:	2
License:	MIT
Group:		Networking
Source0:	http://downloads.sourceforge.net/synce/gcemirror-%{version}.tar.gz
# Source0-md5:	7589d3a914aa35d922edb0827d9878fa
URL:		http://www.synce.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	synce-core-lib-devel >= 0.17
Requires:	synce-core-lib >= 0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ based remote viewer and controller, in the vein of VNC.

The display of the Windows CE device is captured and transfered to the
desktop where it gets displayed in a window. The user now can interact
via this window by using the mouse and the keyboard of the desktop.

%description -l pl.UTF-8
Oparte na GTK+ narzędzie do zdalnego podglądu i sterowania podobne do
VNC.

Ekran Windows CE jest przechwytywany i przesyłany na komputer
stacjonarny, gdzie jest wyświetlany w okienku. Użytkownik może
wykonywać operacje poprzez to okienko przy użyciu myszy i klawiatury
komputera stacjonarnego.

%description -l ru.UTF-8
GCeMirror предоставляет способ интерактивного взаимодействия с
PocketPC.

Дисплей устройства захватывается и передается на ПК для отображения, а
ввод с помощью клавиатуры и мыши возвращается Windows CE.

%description -l uk.UTF-8
GCeMirror надає можливість інтерактивної взаємодії із PocketPC.

Дісплей пристрою захоплюється із передачею на ПК для відображення, а
ввод за допомогою клавіатури та миші повертається до Windows CE.

%prep
%setup -q -n gcemirror-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%find_lang gcemirror

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gcemirror.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/gcemirror
%{_mandir}/man1/gcemirror.1*
# XXX dir included also by synce-serial
%dir %{_datadir}/synce
%{_datadir}/synce/screensnap.exe.arm
%{_datadir}/synce/screensnap.exe.mips
%{_datadir}/synce/screensnap.exe.sh3
