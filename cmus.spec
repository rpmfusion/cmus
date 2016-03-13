Name:           cmus
Version:        2.7.1
Release:        1%{?dist}
Summary:        Ncurses-Based Music Player
Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://cmus.github.io/
Source0:        https://github.com/cmus/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  flac-devel
BuildRequires:  libao-devel
BuildRequires:  libcue-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opusfile-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  wavpack-devel

BuildRequires:  ncurses-devel


%description
cmus is a small, fast and powerful console music player for Unix-like
operating systems


%prep
%setup -q


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
  CONFIG_MP4=y \
  CONFIG_MPC=y \
  CONFIG_OPUS=y \
  CONFIG_OSS=n \
  CONFIG_PULSE=y \
  CONFIG_ROAR=n \
  CONFIG_SUN=n \
  CONFIG_VORBIS=y \
  CONFIG_WAV=y \
  CONFIG_WAVEOUT=n \
  CONFIG_WAVPACK=y \
  CFLAGS="%{optflags}"
make %{?_smp_mflags} V=2


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples .
chmod -x examples/*


%files
%doc COPYING AUTHORS examples
%{_bindir}/%{name}
%{_bindir}/cmus-remote
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/cmus-remote.1*
%{_mandir}/man1/cmus.1*
%{_mandir}/man7/cmus-tutorial.7*


%changelog
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
