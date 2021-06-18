%global app                     mysql
%global user                    %{app}
%global group                   %{app}

%global d_home                  /home
%global d_storage               %{d_home}/storage.01
%global d_data                  %{d_storage}/data.02

%global d_cnf                   %{_sysconfdir}/mysql
%global d_service               %{_sysconfdir}/systemd/system/mysqld.service.d

%global release_prefix          100

Name:                           ext-mysql
Version:                        1.0.4
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure MySQL
License:                        MIT
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source10:                       my.cnf
Source20:                       service.limits.conf

Requires:                       mysql-community-server ext-system

%description
META-package for install and configure MySQL.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -dp -m 0755 %{buildroot}%{d_data}/%{app}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_cnf}/my.cnf
%{__install} -Dp -m 0644 %{SOURCE20} \
  %{buildroot}%{d_service}/custom.limits.conf


%files
%attr(0700,%{user},%{group}) %dir %{d_data}/%{app}
%dir %{d_cnf}
%config %{d_cnf}/my.cnf
%config %{d_service}/custom.limits.conf


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.4-100
- UPD: Move to GitHub.
- UPD: License.

* Tue Nov 12 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-100
- UPD: Directory names.

* Sun Jul 28 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-103
- UPD: SPEC-file.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-102
- UPD: SPEC-file.
- FIX: Systemd Drop-In.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-101
- UPD: SPEC-file.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- NEW: Systemd config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-110
- UPD: MySQL config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-109
- UPD: MySQL config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-108
- UPD: MySQL config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-107
- UPD: MySQL config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-106
- UPD: MySQL config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-105
- UPD: MySQL config.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-104
- UPD: MySQL config.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-103
- UPD: MySQL config.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-102
- UPD: SPEC-file.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-101
- UPD: MySQL config.

* Thu Jul 04 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- FIX: Config files.
- UPD: SPEC-file.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-102
- UPD: SPEC-file.

* Mon Jul 01 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- UPD: MySQL config.

* Sat Jun 22 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
