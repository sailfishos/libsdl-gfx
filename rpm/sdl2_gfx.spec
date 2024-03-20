Summary: Simple DirectMedia Layer - Graphics Primitives
Name: SDL2_gfx
Version: 1.0.4
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/sdl2gfx/
License: zlib
BuildRequires: pkgconfig(sdl2)

%description
Library containing 20+ graphics primitives (line, box, circle,
polygon, etc.) for SDL2.

%package devel
Summary: Simple DirectMedia Layer - Graphics Primitives (Development)
Requires: %{name} = %{version}

%description devel
Library containing 20+ graphics primitives (line, box, circle,
polygon, etc.) for SDL2.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
# Fix a build error in OBS (see http://stackoverflow.com/q/10085554)
autoreconf -fvi
%configure \
%ifnarch %{ix86} %{x86_64} x86_64
          --disable-mmx \
%endif
          --disable-static
# On non-X86 architectures, disable MMX
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root)
%license COPYING
%doc AUTHORS INSTALL NEWS README
%{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root)
%doc AUTHORS INSTALL NEWS README
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*/*.h

