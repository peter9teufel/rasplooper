#!/bin/sh

echo "Removing not used wolfram engine..."
# remove not used wolfram-engine
sudo apt-get -y remove wolfram-engine;

echo "Updating sources and system..."
# update apt sources and upgrade installed packages
sudo apt-get -y update;
sudo apt-get -y upgrade;

echo "Installing required packages..."

# install usbmount, could be usable for future updates
sudo apt-get -y install usbmount;

echo "";
echo "Cloning RaspLooper source from github";
# clone raspmedia sourcefiles to /home/pi/raspmedia
cd /home/pi;
su -l pi -c 'git clone https://github.com/peter9teufel/rasplooper.git';

echo "";
echo "Writing boot config...";
sudo cat /home/pi/rasplooper/rasplooper_boot_config.txt > /boot/config.txt;
echo "";

echo "Setting up autostart of RaspLooper Player";
# modify rc.local to start raspmedia at boot
sudo head -n -2 /etc/rc.local > /home/pi/rc.local.tmp;
sudo cat /home/pi/rc.local.tmp > /etc/rc.local;
sudo echo 'sudo /home/pi/rasplooper/scripts/img_install_postprocess.sh' >> /etc/rc.local;
sudo echo 'exit 0' >> /etc/rc.local;
sudo rm /home/pi/rc.local.tmp;

sudo raspi-config;

echo 'Setup complete!';
echo 'Rebooting...';
sudo reboot;

# install script deletes itself after completion
rm -- "$0"
