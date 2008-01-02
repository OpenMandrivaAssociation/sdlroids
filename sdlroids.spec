%define	name	sdlroids
%define	version	1.3.4
%define	release	%mkrel 9
%define	Summary	SDLRoids - an enhanced shoot-the-asteroids

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source0:	%{name}-%{version}.tar.bz2
URL:		http://eongames.com/games/sdlroids/
Buildrequires:	SDL1.2-devel ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SDLRoids is essentially an Asteroids clone, but with a few extra
features, and some nice game physics. It is based on xhyperoid, which
is a UNIX port of the 16-bit Windows game Hyperoid. Major changes from
xhyperoid are that it's using SDL for sound and graphics, has a couple
of extra powerups  and that the shield behaves differently.

%prep
%setup -q

%build
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--disable-rpath
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir} datadir=$RPM_BUILD_ROOT%{_gamesdatadir}

%{__install} -d $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir}}
convert icons/%{name}-16x16.xpm $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert icons/%{name}-32x32.xpm $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert icons/%{name}-48x48.xpm $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}                
Icon=%{name}                                
Categories=Game;ArcadeGame;                
Name=SDLRoids                
Comment=%{Summary}
EOF

%post
%update_menus
  
%postun
%clean_menus 


%clean
rm -rf $RPM_BUILD_ROOT

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

