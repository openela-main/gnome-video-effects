Name:           gnome-video-effects
Version:        0.4.3
Release:        3%{?dist}
Summary:        Collection of GStreamer video effects

Group:          System Environment/Libraries
License:        GPLv2
URL:            https://wiki.gnome.org/Projects/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.4/%{name}-%{version}.tar.xz
Buildarch:      noarch

BuildRequires:  intltool

Requires:       frei0r-plugins

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS NEWS README
%license COPYING
%{_datadir}/pkgconfig/gnome-video-effects.pc
%{_datadir}/gnome-video-effects


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Kalev Lember <klember@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Mon Oct 10 2016 Hans de Goede <hdegoede@redhat.com> - 0.4.1-5
- Fix URL (rhbz#1380981)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Richard Hughes <rhughes@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep  8 2012 Hans de Goede <hdegoede@redhat.com> - 0.4.0-4
- Drop Requires for gstreamer-plugins, as we may be used with both
  gstreamer-0.10 and 1.0. Instead apps using gnome-video-effects should add
  the necessary Requires themselves

* Fri Aug 24 2012 Hans de Goede <hdegoede@redhat.com> - 0.4.0-3
- Add Requires for the gstreamer-plugins used by the effects (related#850505)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Yanko Kaneti <yaneti@declera.com> 0.4.0-1
- Update to 0.4.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Yanko Kaneti <yaneti@declera.com> 0.3.0-1
- Update to 0.3.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Yanko Kaneti <yaneti@declera.com> 0.2.0-1
- Update to 0.2.0. New effects.

* Wed Sep  1 2010 Yanko Kaneti <yaneti@declera.com> 0.1.0-1
- Packaged for review
