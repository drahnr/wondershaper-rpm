%{!?COMMIT_SHA: %define COMMIT_SHA 5e8359464938163f2a308710c3f489e2e5d9a7c8}

Name:		wondershaper
Version:	1.4.0
Release:	3%{?dist}
Summary:	Simple Network Shaper
Group:		Applications/Internet
License:	GPLv2+
URL:		https://github.com/magnific0/wondershaper
Source0:	https://github.com/magnific0/wondershaper/archive/%{COMMIT_SHA}.tar.gz
Source1:	wondershaper.service

Requires:	iproute
Requires:	kernel-modules-extra
%{?systemd_requires}
BuildRequires:   systemd
BuildArch:	noarch

%description
Many cable-modem and ADSL users experience horrifying latency
while uploading or downloading. They also notice that uploading
hampers downloading greatly. The Wondershaper neatly addresses
these issues, allowing users of a router with a Wondershaper to
continue using SSH over a loaded link happily.

%prep
%setup -q -n %{name}-%{COMMIT_SHA}

%build
# nothing

%install
install -pDm 755 %{name} %{buildroot}/%{_bindir}/%{name}
rm %{name}.service
install -pDm 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -pDm 644 %{name}.conf %{buildroot}/%{_sysconfdir}/conf.d/%{name}.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config %{_sysconfdir}/conf.d/%{name}.conf

%changelog
* Fri Mar 27 2020 Bernhard Schuster - 1.4.0-3
- Assure systemd service file does handle rate updates in the config file

* Thu Dec 27 2018 Bernhard Schuster - 1.4.0-2
- Require COMMITSHA to be passed from command line

* Sun Jul 15 2018 Bernhard Schuster - 1.4.0-1
- Change of upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 8 2015 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.1-5
- Fix #1209243
- Use %%license

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.1-2
- Fix package git commit.

* Tue Nov 19 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2.1-1
- Update to 1.2.1 .
- Replace URL with main program page.
- General tweaks.
- Remove VERSION file from %%doc.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-3
- Remove permissions line.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-2
- To zero warnings by rpmlint.

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.2-1
- NG of wondershaper , update to version 1.2 

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.1a-6
- Fixes to be compatible with Fedora rules.

* Sun Sep 23 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.1a-5.1
- Initial build for Kenzi.

* Thu Aug 7 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.1a-2
- Initial package release.
