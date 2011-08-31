#!/bin/bash

# This script downloads the links in the file $SRC. Written to be used as a cron job, but still has to hack.


SRC=links

if [[ ! -r $SRC ]]; then
	echo E: File not found!!
	exit -1
fi

echo I: All good Starting download.

N=0
cat $SRC | while read LINK; do
	echo I: Downloading $N
	N=$((N+1))
	wget "$LINK"
	done

exit 0

