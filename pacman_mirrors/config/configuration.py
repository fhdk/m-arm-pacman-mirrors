#!/usr/bin/env python
#
# This file is part of pacman-mirrors.
#
# pacman-mirrors is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pacman-mirrors is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pacman-mirrors.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Frede Hundewadt <echo ZmhAbWFuamFyby5vcmcK | base64 -d>

"""Pacman-Mirrors Configuration"""

# http constants
URL_MIRROR_JSON = \
    "https://raw.githubusercontent.com/fhdk/m-arm-web-repos/master/mirrors.json"
URL_STATUS_JSON = "http://repo.manjaro.org/status.json"
INET_CONN_CHECK_URLS = ["https://wikipedia.org",
                        "https://github.com",
                        "https://bitbucket.org"]
# etc files
CONFIG_FILE = "/etc/pacman-mirrors.conf"
MIRROR_LIST = "/etc/pacman.d/manjaro-arm-mirrorlist"
# pacman-mirrors dir/files
WORK_DIR = "/var/lib/pacman-mirrors/"
USR_DIR = "/usr/share/pacman-mirrors"
CUSTOM_FILE = "/var/lib/pacman-mirrors/custom-mirrors.json"
MIRROR_FILE = "/usr/share/pacman-mirrors/mirrors.json"
STATUS_FILE = "/var/lib/pacman-mirrors/status.json"
# repo constants
BRANCHES = ("stable", "unstable")
REPO_ARCH = "/$repo/$arch"
# special cases
O_CUST_FILE = "/var/lib/pacman-mirrors/Custom"
TO_BE_REMOVED = "/var/lib/pacman-mirrors/mirrors.json"
# wayland support
TEMP_CONFIG = "pacman-mirrors.conf"
TEMP_CUSTOM = "custom-mirrors.json"
TEMP_MIRROR = "mirrors.json"
TEMP_STATUS = "status.json"
