#!/bin/bash

ADDON_PATH="${HOME}/.config/blender/2.79/scripts/addons"

if [ $# -ne 1 ]; then
    echo "Pass file name as an argument which you want to install."
    exit 1
fi

if [ ! -d $ADDON_PATH ]; then
    mkdir -p $ADDON_PATH
fi

pushd $(dirname $0)
cp $1 $ADDON_PATH
popd
