#!/bin/bash
#
# Set the default gateway, nameservers and date
# automatically. This script needs to be
# called via init.d

## Add a default gateway
/sbin/route add default gw 192.168.7.1

## add the nameservers if necessary
grep -q 8.8.8.8 /etc/resolv.conf
if [ "$?" -ne "0" ]; then
        echo "domain localdomain" > /etc/resolv.conf
        echo "search localdomain" >> /etc/resolv.conf
        echo "nameserver 8.8.4.4" >> /etc/resolv.conf
        echo "nameserver 8.8.8.8" >> /etc/resolv.conf
fi

## End of the settings script