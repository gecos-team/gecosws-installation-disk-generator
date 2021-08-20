# -*- coding: utf-8 -*-
# Config file for master.py

#######
# GIT
#######

# A polling time in seconds to detect changes into git repositories
polling_time = 120

# List with apps names. The name is the same that repository into github organization gecos-team
# If you add a new app builbot managed this

apps_gecos = [
    "gecosws-config-assistant",
    "gecosws-firstart",
    "gecosws-agent",
    "gecoshc-client",
    "gecosws-lightdm-greeter"
]

# List with metapkgs names. The name is the same that repository into github organization gecos-team
# If you add a new metapkgs builbot managed this

metapkgs_gecos = [
     "gecosws-meta",
#     "gecosws-light-meta",
     "gecosws-artwork",
     "gecosws-skel-conf",
#     "gecosws-light-artwork",
#     "gecosws-light-lxde-common-conf",
     "gecosws-mint-artwork-cinnamon-conf",
     "gecosws-mint-artwork-common-conf",
     "gecosws-cinnamon-conf",
     "gecosws-mint-x-icons-conf",
     "gecosws-system-conf",
     "gecosws-xdg-ruby",
     "gecosws-chef-notifier-cinnamon",
     "gecosws-repository-compatibility",
     "gecosws-certificates-locale",
#     "gecosws-chef-snitch",
#     "java-nss-fix",
     "gecosws-conf-lightdm",
     "gecosws-artwork-common",
     "gecosws-fonts",
     "gecosws-plymouth-theme",
     "cups-ad-fix"   
]

metapkgs = [
     "gecosws-icon-theme",
#     "gecosws-mdm-theme",
     "gecosws-artwork-lightdm",
     "gecosws-ubiquity",
]

appimgs = {
        "gecoshc-client" : "helpchannel-1.2.1-x86_64.AppImage"
}

apps = [

]
# Indicates if we should abort the integration process if we have any linitian errors
halt_on_lintian_error = False

# Script live-build
livebuild_gecos = "sudo /var/gensys/live-build/gecosv5/buildgecos.sh"
livebuild_gecos_lite = "sudo /var/gensys/live-build/gecosv5-lite/buildgecoslite.sh"

# Script to build AppImages
# (Install appimage-builder by executing the following commands:
#
#   virtualenv appimage-builder
#   source  appimage-builder/bin/activate
#   pip3 install appimage-builder
#
# It needs to be in a separate virtual environment because there is a
# conflict with python3-yaml version.
appimage_builder = "/var/gensys/appimage-builder/bin/appimage-builder"

# Codename of repository

codename_gecos = "v5"

# Pdebuild custom commands
pdebuild = "pdebuild --configfile /var/gensys/.pbuilderrc"

# Path of own repository
repo_dir_gecos = "/var/gensys/deb-repositories/gecos"

rawimage_gecos = "/var/gensys/live-build/gecosv5/binary.hybrid.iso"
rawimage_gecos_lite = "/var/gensys/live-build/gecosv5-lite/binary.hybrid.iso"
ftpimage_gecos = "/var/gensys/deb-repositories/isos/gecos-desktop-64bits.iso"
ftpimage_gecos_lite = "/var/gensys/deb-repositories/isos/gecos-lite-desktop-32bits.iso"
ftpimage_appimgs = "/var/gensys/deb-repositories/appimgs"


gensys_gecos_time = "04:00"
gensys_gecos_lite_time = "06:00"

