
Name:    compat-exiv2-023
Version: 0.23
Release: 2%{?dist}
Summary: Compatibility package with the exiv2 library in version 0.23

License: GPLv2+
URL:     http://www.exiv2.org/
Source0: http://www.exiv2.org/exiv2-%{version}.tar.gz

## upstream patches

BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: zlib-devel

Conflicts: exiv2-libs < 0.26

%description
Compatibility package with the exiv2 0.23 ABI. It is meant to work with
applications and libraries using exiv2 and build prior to exiv2 0.26 update.


%prep
%setup -q -n exiv2-%{version}

%build
%configure \
  --disable-rpath \
  --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

## Unpackaged files
rm -rf %{buildroot}%{_bindir}/exiv2
rm -rf %{buildroot}%{_libdir}/libexiv2.la
rm -rf %{buildroot}%{_datadir}/locale/*
rm -rf %{buildroot}%{_mandir}/*
rm -rf %{buildroot}%{_libdir}/pkgconfig/exiv2.pc
rm -rf %{buildroot}%{_includedir}/exiv2
rm -rf mv %{buildroot}%{_libdir}/libexiv2.so

## fix perms on installed lib
ls -l     %{buildroot}%{_libdir}/libexiv2.so.*
chmod 755 %{buildroot}%{_libdir}/libexiv2.so.*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/libexiv2.so.12*


%changelog
* Mon Jun 18 2018 Jan Grulich <jgrulich@redhat.com> - 0.23-2
- Remove Windows binaries from the tarball
  Resolves: bz#1568618

* Wed Jun 13 2018 Jan Grulich <jgrulich@redhat.com> - 0.23-1
- Spec file based on exiv2 package to provide old libraries before API change
  Resolves: bz#1568618

