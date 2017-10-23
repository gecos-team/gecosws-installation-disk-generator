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
]

# List with metapkgs names. The name is the same that repository into github organization gecos-team
# If you add a new metapkgs builbot managed this

#metapkgs_gv9 = [
#    "guadalinexv9-meta",
#    "guadalinexv9-light-meta",
#    "guadalinexv9-artwork",
#    "guadalinexv9-skel-conf",
#    "guadalinexv9-help-mantis",
#    "guadalinexv9-light-artwork",
#    "guadalinexv9-light-lxde-common-conf",
#    "guadalinexv9-mint-artwork-cinnamon-conf",
#    "guadalinexv9-mint-artwork-common-conf",
#    "guadalinexv9-mint-x-icons-conf",
#    "guadalinexv9-casper-conf",
#    "guadalinexv9-ubiquity-conf",
#    "guadalinexv9-cinnamon-conf",
#    "guadalinexv9-firefox-24.2.0",
#    "guadalinexv9-thunderbird-esr",
#    "guadalinexv9-thunderbird-esr-conf",
#    "guada-firefox-cert",
#    "ubiquity-slideshow-guada",

#    "meta-guadalinexv9-light",
#    "meta-gecosv2",
#    "meta-gecosv2-light",
#]

metapkgs_gecos = [
     "gecosws-meta",
     "gecosws-light-meta",
     "gecosws-artwork",
     "gecosws-skel-conf",
     "gecosws-light-artwork",
     "gecosws-light-lxde-common-conf",
     "gecosws-mint-artwork-cinnamon-conf",
     "gecosws-mint-artwork-common-conf",
     "gecosws-cinnamon-conf",
     "gecosws-mint-x-icons-conf",
     "gecosws-system-conf",
     "gecosws-xdg-ruby",
     "gecosws-chef-notifier-cinnamon",
     "gecosws-repository-compatibility",
     "gecosws-certificates-locale",
     "ca-certificates-es",
#     "gecosws-chef-snitch",
     "java-nss-fix",
     "cups-ad-fix"   
]

metapkgs = [
     "gecosws-icon-theme",
     "gecosws-mdm-theme",
#     "gecosws-firerfox-wrapper",
     "gecosws-ubiquity",
#     "guadalinexv9-firefox-24.2.0-32",
]

apps = [

]
# Indicates if we should abort the integration process if we have any linitian errors
halt_on_lintian_error = False

# Script live-build
#livebuild_gv9 = "sudo /var/gensys/live-build/guadalinexv9/buildv9.sh"
#livebuild_gv9_light = "sudo /var/gensys/live-build/guadalinexv9-light/buildv9-light.sh"
livebuild_gecos = "sudo /var/gensys/live-build/gecosv3/buildgecos.sh"
livebuild_gecos_lite = "sudo /var/gensys/live-build/gecosv3-lite/buildgecoslite.sh"

# Codename of repository
#codename_v9 = "quebrantahuesos"

codename_gecos = "v3"

# Pdebuild custom commands
#pdebuild = "pdebuild --configfile /var/gensys/.pbuilderrc"
pdebuild = "pdebuild --configfile /var/gensys/.pbuilderrc"

# Path of own repository
#repo_dir_guada = "/var/gensys/deb-repositories/guadalinex"
#repo_dir_guada_trusty = "/var/gensys/deb-repositories/guadalinex-trusty"
repo_dir_gecos = "/var/gensys/deb-repositories/gecos"
#repo_dir_gecos_trusty = "/var/gensys/deb-repositories/gecos"

#rawimage_gv9 = "/var/gensys/live-build/guadalinexv9/binary.hybrid.iso"
#ftpimage_gv9 = "/var/gensys/deb-repositories/isos/guadalinexv9-desktop-32bits.iso"
#rawimage_gv9_light = "/var/gensys/live-build/guadalinexv9-light/binary.hybrid.iso"
#ftpimage_gv9_light = "/var/gensys/deb-repositories/isos/guadalinexv9-light-desktop-32bits.iso"
rawimage_gecos = "/var/gensys/live-build/gecosv3/binary.hybrid.iso"
rawimage_gecos_lite = "/var/gensys/live-build/gecosv3-lite/binary.hybrid.iso"
ftpimage_gecos = "/var/gensys/deb-repositories/isos/gecos-desktop-64bits.iso"
ftpimage_gecos_lite = "/var/gensys/deb-repositories/isos/gecos-lite-desktop-32bits.iso"


#gensys_gv9_time = "00:00"
#gensys_gv9_lite_time = "02:00"
gensys_gecos_time = "04:00"
gensys_gecos_lite_time = "06:00"

