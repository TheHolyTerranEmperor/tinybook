#!/bin/sh

#enable spi?
sed -i '/dtparam=spi=on/s/^#//g' /boot/config.txt

#install lg library
wget https://github.com/joan2937/lg/archive/master.zip
unzip master.zip
cd lg-master
make
make install

