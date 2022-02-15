#!/bin/bash

# Move files into the appropriate directories
mv ./configFiles/internet_config.sh /home/debian/bin/
mv ./configFiles/pin_config.sh /home/debian/bin/
mv ./configFiles/pin_config.service /home/debian/bin/
mv ./configFiles/setup.sh /home/debian/bin/
mv ./configFiles/internet_config /etc/init.d/

# Set permission for file
chmod 755 /etc/init.d/internet_config

# Prep config file
ln -s /home/debian/bin/pin_config.service /etc/systemd/system/pin_config.service
chmod +x /home/debian/bin/*.sh

# Run config files
bash /home/debian/bin/pin_config.sh
bash /home/debian/bin/setup.sh
sudo bash /home/debian/bin/internet_config.sh

# Create a symbolic link to init network settings on boot
ln -s /etc/init.d/internet_config /etc/rc5.d/S99internet_config

# Reload sources
source /home/debian/.bashrc
systemctl daemon-reload
systemctl enable pin_config
/etc/init.d/networking restart
echo "Waiting for network"
sleep 10

if ping -q -c 1 -W 1 google.com >/dev/null; then
  echo "The network is up"
  echo "Waiting for cache to update"
  sleep 15
  #echo "You might want to just check back later"
  #sleep 60
  sudo apt update
  sudo apt install libgpiod-dev libgpiod2 -y
  #sudo apt upgrade -y
  cd /var/lib/cloud9/PocketBeagle/PocketBeagle_RSLK/src/
  gcc -shared -o sensor.so -fPIC lineSensor.c -lgpiod
  gcc -shared -o leds.so -fPIC CTRLlines.c -lgpiod
  gcc -shared -o distance.so -fPIC distanceSensor.c -lgpiod
  mkdir c_files
  mv *.c c_files
  mkdir sharedlib
  mv *.so sharedlib
  ln -s sharedlib/sensor.so /usr/include/
  ln -s sharedlib/leds.so /usr/include/
  ln -s sharedlib/distance.so /usr/include/
  rm -rf /var/lib/cloud9/configFiles
else
  echo "The network is down"
  echo "Please recheck your network settings on your Windows computer"
  exit
fi

echo "The installation is now complete. Enjoy!"
#echo "The installation is now complete. Rebooting..."
#reboot


