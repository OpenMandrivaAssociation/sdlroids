Summary:	- an enhanced shoot-the-asteroids
Name:		sdlroids
Version:	1.3.4
Release:	14
License:	GPL
Group:		Games/Arcade
Source0:	%{name}-%{version}.tar.bz2
URL:		http://eongames.com/games/sdlroids/
BuildRequires:	pkgconfig(sdl)
BuildRequires:	imagemagick

%description
SDLRoids is essentially an Asteroids clone, but with a few extra
features, and some nice game physics. It is based on xhyperoid, which
is a UNIX port of the 16-bit Windows game Hyperoid. Major changes from
xhyperoid are that it's using SDL for sound and graphics, has a couple
of extra powerups  and that the shield behaves differently.

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-rpath
%make

%install
%makeinstall bindir=%{buildroot}%{_gamesbindir} datadir=%{buildroot}%{_gamesdatadir}

install -d %{buildroot}{%{_liconsdir},%{_miconsdir}}
convert icons/%{name}-16x16.xpm %{buildroot}%{_miconsdir}/%{name}.png
convert icons/%{name}-32x32.xpm %{buildroot}%{_iconsdir}/%{name}.png
convert icons/%{name}-48x48.xpm %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}                
Icon=%{name}                                
Categories=Game;ArcadeGame;                
Name=SDLRoids                
Comment=SDLRoids - an enhanced shoot-the-asteroids
EOF

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.orig README.xhyperoid COPYING
%{_mandir}/man6/%{name}.6*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}

