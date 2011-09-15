#!/bin/bash

# This script downloads the links in the html file given as argument.
#  

SRC=links
URL=$1

TYPE=avi  # File type to download.

if [[ ! -r $URL ]]; then
	echo E: No input file found!!
	echo Usage: $0 <html file>
	exit -1
else
	./list_links.sed $URL | grep *.$TYPE > $SRC 
fi

if [[ ! -r $SRC ]]; then
	echo E: File not found!!
	exit -1
fi

echo I: All good, Starting download.

N=0
cat $SRC | while read LINK; do
	echo I: Downloading $N
	N=$((N+1))
	wget -c "$LINK"
	done
echo I: Download complete, Cleaning Up.
rm $SRC
exit 0

