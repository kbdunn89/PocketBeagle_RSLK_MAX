#!/bin/bash

echo "alias internet='sudo /var/lib/cloud9/internet_config.sh'" >> ~/.bashrc
echo "alias update='sudo apt update && sudo apt upgrade -y'" >> ~/.bashrc
echo "alias USB1='echo 1 > /sys/bus/usb/devices/2-1.1/bConfigurationValue" >> ~/.bashrc
echo "alias USB2='echo 1 > /sys/bus/usb/devices/2-1.2/bConfigurationValue" >> ~/.bashrc

source ~/.bashrc
