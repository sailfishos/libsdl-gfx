Summary: Simple DirectMedia Layer - Graphics Primitives
Name: SDL2_gfx
Version: 1.0.4
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/sdl2gfx/
License: zlib
Group: Applications/Multimedia
BuildRequires: pkgconfig(sdl2)

%description
Library containing 20+ graphics primitives (line, box, circle,
polygon, etc.) for SDL2.

%package devel
Summary: Simple DirectMedia Layer - Graphics Primitives (Development)
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Library containing 20+ graphics primitives (line, box, circle,
polygon, etc.) for SDL2.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
# Fix a build error in OBS (see http://stackoverflow.com/q/10085554)
autoreconf -fvi
%configure
%make_build

%install
%make_install

find %{buildroot} -name \*.a -delete

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root)
%doc AUTHORS INSTALL NEWS README
%{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root)
%doc AUTHORS INSTALL NEWS README
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*/*.h

