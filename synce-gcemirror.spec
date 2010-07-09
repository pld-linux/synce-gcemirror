Summary:	Windows CE remote control tool like VNC
Summary(pl.UTF-8):	Narzędzie do sterowania Windows CE podobne do VNC
Summary(ru.UTF-8):	Управление Windows CE в стиле VNC
Summary(uk.UTF-8):	Керування Windows CE у стилі VNC
Name:		synce-gcemirror
Version:	0.2
Release:	1
License:	MIT
Group:		Networking
Source0:	http://downloads.sourceforge.net/project/synce/SynCE-GNOME/0.15/gcemirror-%{version}.tar.gz
# Source0-md5:	900d32314242ca95ab94637c424573e3
URL:		http://www.synce.org/
BuildRequires:	gtk+2-devel >= 1:2.14
BuildRequires:	libjpeg-devel
BuildRequires:	synce-librapi2-devel >= 0.13
BuildRequires:	synce-libsynce-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK based remote viewer and controller, in the vein of VNC.

The display of the Windows CE device is captured and transfered to the
desktop where it gets displayed in a window. The user now can interact
via this window by using the mouse and the keyboard of the desktop.

%description -l pl.UTF-8
KCeMirror udostępnia metodę współpracy z urządzeniem PocketPC poprzez
środowisko graficzne.

Ekran Windows CE jest przechwytywany i przesyłany na komputer
stacjonarny, gdzie jest wyświetlany w okienku. Użytkownik może
wykonywać operacje poprzez to okienko przy użyciu myszy i klawiatury
komputera stacjonarnego.

%description -l ru.UTF-8
KCeMirror предоставляет способ интерактивного взаимодействия с
PocketPC.

Дисплей устройства захватывается и передается на ПК для отображения, а
ввод с помощью клавиатуры и мыши возвращается Windows CE.

%description -l uk.UTF-8
KCeMirror надає можливість інтерактивної взаємодії із PocketPC.

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
