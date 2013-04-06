Name:		brewtarget
Version:	2.0.1
Release:	4%{?dist}
Summary:	An open source beer recipe creation tool
Group:		Applications/Productivity
License:	GPLv3 and WTFPL and LGPLv2
URL:		http://www.brewtarget.org
Source0:        https://launchpad.net/brewtarget/trunk/%{version}/+download/brewtarget_%{version}.orig.tar.gz

BuildRequires:	cmake
BuildRequires:	qt-devel
BuildRequires:	qt-webkit-devel
BuildRequires:	phonon-devel
BuildRequires:	desktop-file-utils
BuildRequires:	sqlite
%description
Brewtarget is an open source beer recipe creation tool. It automatically 
calculates color, bitterness, and other parameters for you while you drag and 
drop ingredients into the recipe. Brewtarget also has many other tools such as 
priming sugar calculators, OG correction help, and a unique mash designing tool. 
It also can export and import recipes in BeerXML.

%prep
%setup -q

%build
%cmake -DDO_RELEASE_BUILD:BOOL=ON 
make %{?_smp_mflags} 

%install
make VERBOSE=1 INSTALL="install -p" CP="cp -p" DESTDIR=%{buildroot} install
/usr/bin/install -m 0644 -Dp doc/brewtarget.1 %buildroot%{_mandir}/man1/brewtarget.1
desktop-file-validate %buildroot%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}
%{_mandir}/man1/brewtarget.1*
%doc README COPYRIGHT COPYING.GPLv3 COPYING.WTFPL doc/manual/index.html 

%changelog
* Sat Apr 06 2013 Philip Lee <rocketman768@gmail.com> 2.0.1-1
- Removed all patches since they have been integrated upstream.
- Changed upstream source location.

* Sun Nov 18 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.3-4
- Fixing permissions on manpage

* Sat Nov 17 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-3
- Including bundled manpage, updating SPEC

* Fri Nov 16 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-2
- Changes to SPEC file per packaging guidelines.

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Initial build of 1.2.5 release

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Added patch to correct .desktop file

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Added patch to install documentation to appropriate directory

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Patching to warn if no documentation instead of exit.

