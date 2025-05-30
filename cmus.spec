%global commit0 89f1c935cbc0a345b796507bdc52c76086ecc26b
%global date 20240324
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

%global surl https://github.com/cmus/cmus

Name:           cmus
Version:        2.12.0
Release:        3%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Ncurses-Based Music Player
License:        GPLv2+
URL:            https://cmus.github.io/
%if 0%{?tag:1}
Source0:        %surl/archive/v%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %surl/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  alsa-lib-devel
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  flac-devel
BuildRequires:  libao-devel
BuildRequires:  libcddb-devel
BuildRequires:  libcue-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opusfile-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd-devel
BuildRequires:  wavpack-devel
BuildRequires:  ncurses-devel


%description
cmus is a small, fast and powerful console music player for Unix-like
operating systems


%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif


%build
./configure prefix=%{_prefix} bindir=%{_bindir} datadir=%{_datadir} \
  libdir=%{_libdir} mandir=%{_mandir} \
  exampledir=%{_datadir}/%{name}/examples \
  CONFIG_AAC=y \
  CONFIG_ALSA=y \
  CONFIG_AO=y \
  CONFIG_ARTS=n \
  CONFIG_CDIO=n \
  CONFIG_CUE=y \
  CONFIG_FFMPEG=y \
  CONFIG_FLAC=y \
  CONFIG_JACK=n \
  CONFIG_MAD=y \
  CONFIG_MIKMOD=n \
  CONFIG_MODPLUG=y \
  CONFIG_MPC=y \
  CONFIG_MPRIS=y \
  CONFIG_OPUS=y \
  CONFIG_OSS=n \
  CONFIG_PULSE=y \
  CONFIG_ROAR=n \
  CONFIG_SUN=n \
  CONFIG_VORBIS=y \
  CONFIG_WAV=y \
  CONFIG_WAVEOUT=n \
  CONFIG_WAVPACK=y \
  CFLAGS="${RPM_OPT_FLAGS}" \
  LDFLAGS="${RPM_LD_FLAGS}"
%{make_build} V=2


%install
# Using the make_install macro causes the build to fail
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples .
chmod -x examples/*


%files
%doc AUTHORS examples
%license COPYING
%{_bindir}/%{name}
%{_bindir}/cmus-remote
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/cmus-remote.1*
%{_mandir}/man1/cmus.1*
%{_mandir}/man7/cmus-tutorial.7*


%changelog
* Fri May 30 2025 Leigh Scott <leigh123linux@gmail.com> - 2.12.0-3
- Rebuild for new flac .so version

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Leigh Scott <leigh123linux@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Sat Oct 12 2024 Leigh Scott <leigh123linux@gmail.com> - 2.11.0-3
- rebuild for ffmpeg

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 12 2024 Leigh Scott <leigh123linux@gmail.com> - 2.11.0-1
- Update to 2.11.0

* Tue May 07 2024 Leigh Scott <leigh123linux@gmail.com> - 2.10.1-0.1.20240324git89f1c93
- Update to git snapshot

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 08 2023 Leigh Scott <leigh123linux@gmail.com> - 2.10.0-7
- Rebuild for new faad2 version

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 26 2023 Leigh Scott <leigh123linux@gmail.com> - 2.10.0-5
- rebuilt

* Tue Feb 28 2023 Leigh Scott <leigh123linux@gmail.com> - 2.10.0-4
- Rebuild for new ffmpeg

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 2.10.0-3
- Rebuild for new flac

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Jul 06 2022 Leigh Scott <leigh123linux@gmail.com> - 2.10.0-1
- Update to 2.10.0 release

* Mon May 09 2022 Sérgio Basto <sergio@serjux.com> - 2.9.1-6
- Remove libmp4v2 dependency

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 2.9.1-4
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Feb 01 2021 Leigh Scott <leigh123linux@gmail.com> - 2.9.1-1
- Update to 2.9.1 release

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 2.8.0-6
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.0-4
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 2.8.0-2
- Rebuild for new ffmpeg version

* Wed Mar 27 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-1
- Update to 2.8.0 release

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.0-0.12.rc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.0-0.11.rc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.0-0.10.rc0
- Rebuilt for new ffmpeg snapshot

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.0-0.9.rc0
- Rebuilt for new ffmpeg snapshot

* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.8.0-0.8.rc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-0.7.rc0
- Rebuilt for ffmpeg-3.5 git

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-0.6.rc0
- Fix install issue

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.8.0-0.5.rc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-0.4.rc0
- Rebuild for ffmpeg update

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.8.0-0.3.rc0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-0.2.rc0
- Add build requires systemd-devel
- Enable MPRIS support

* Sun Dec 04 2016 leigh scott <leigh123linux@googlemail.com> - 2.8.0-0.1.rc0
- Update to 2.8.0-rc0

* Tue Aug 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.7.1-4
- Add build requires libsamplerate-devel and libcddb-devel

* Tue Aug 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.7.1-3
- Fix hardening
- Spec file fixes (rfbz#4194)

* Wed Jul 27 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.7.1-2
- patch for newer ffmpeg

* Fri Dec 04 2015 Sérgio Basto <sergio@serjux.com> - 2.7.1-1
- Update to 2.7.1

* Thu Jun 04 2015 Markus Rothe <markusr815@gmail.com> - 2.6.0-1
- Update to 2.6.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-5
- Rebuilt

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-4
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-2
- Rebuilt for x264/FFmpeg

* Sun Dec 30 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-1
- Update to 2.5.0
- Add BR libcue-devel

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.4.2-4
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 03 2011 Nicolas Chauvet <kwizart@gmail.com> - 2.4.2-2
- Rebuilt for FFmpeg-0.8

* Tue Jul 26 2011 Conrad Meyer <konrad@tylerc.org> - 2.4.2-1
- Bump to latest version
- Drop ffmpeg patch (fixed in 2.4.1+)
- Fixes some bugs

* Wed May 11 2011 Conrad Meyer <konrad@tylerc.org> - 2.4.0-2
- Include configure patch to find ffmpeg.

* Mon Apr 25 2011 Johannes Weißl <jargon@molb.org> - 2.4.0-1
- New upstream release.

* Wed Apr 20 2011 Johannes Weißl <jargon@molb.org> - 2.3.5-1
- New upstream release

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.2.0-4
- rebuild for new F11 features

* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 2.2.0-3
- Make more verbosely (V=2).

* Tue Dec 16 2008 Conrad Meyer <konrad@tylerc.org> - 2.2.0-2
- Build ffmpeg support with gentoo patch.
- Remove libmikmod.

* Sun Nov 16 2008 Conrad Meyer <konrad@tylerc.org> - 2.2.0-1
- Initial package.
