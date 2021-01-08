#!/bin/bash

[ $UID != 0 ] && echo "Inicialo con sudo" && exit 1


_LB_PATH=/var/gensys/live-build/gecosv5

# Live Build from Ubuntu installed in root system
#PATH=${_LB_PATH}/bin:$PATH
#export PATH

LB=lb

_ACT_PATH=$(pwd)

_BUILD_DATE=$(date +%Y%m%d-%H%M)
_LOG_FILE="$_LB_PATH/log/lb_build-$_BUILD_DATE.log"
test -h $_LB_PATH/log/lb_build.log && rm $_LB_PATH/log/lb_build.log
ln -s $_LOG_FILE $_LB_PATH/log/lb_build.log


pushd ${_LB_PATH}
LIVE_BUILD=${_LB_PATH} ${LB} clean 2>&1 | tee -a ${_LOG_FILE}
LIVE_BUILD=${_LB_PATH} ${LB} config 2>&1 | tee -a ${_LOG_FILE}
#LIVE_BUILD=${_LB_PATH} ${LB} config --bootstrap debootstrap 2>${_ERROR_LOG_FILE} | tee -a ${_LOG_FILE}
LIVE_BUILD=${_LB_PATH} ${LB} build 2>&1 | tee -a ${_LOG_FILE}
#LIVE_BUILD=${_LB_PATH} lb bootstrap 2>>${_ERROR_LOG_FILE} | tee -a ${_LOG_FILE}
#LIVE_BUILD=${_LB_PATH} lb chroot 2>>${_ERROR_LOG_FILE} | tee -a ${_LOG_FILE}
#LIVE_BUILD=${_LB_PATH} lb binary 2>>${_ERROR_LOG_FILE} | tee -a ${_LOG_FILE}
#LIVE_BUILD=${_LB_PATH} lb source 2>>${_ERROR_LOG_FILE} | tee -a ${_LOG_FILE}
#popd ${_ACT_PATH}
popd

mount -o loop ${_LB_PATH}/binary.hybrid.iso /srv/gecos-desktop.mnt
rm -fr /srv/gecos-desktop
mkdir -p /srv/gecos-desktop
cp -a /srv/gecos-desktop.mnt/* /srv/gecos-desktop
cp -a /srv/gecos-desktop.mnt/.disk /srv/gecos-desktop/.disk
cp -a /srv/gecos-desktop.mnt/preseed/* /var/gensys/deb-repositories/isos/preseed-gecos/
umount /srv/gecos-desktop.mnt
