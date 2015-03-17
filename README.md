# RaspLooper Video Loop Player for Raspberry Pi

## Overview ##
RaspLooper is a simple solution to bring video files to a Raspberry Pi which are played in an endless loop. That's all the player does, not more and not less. No configuration is needed.

## Installation - Step By Step##

* Flash Raspbian on your RPi SD Card (Google how to do that)
* SSH to your RPi or connect keyboard/monitor
* Run `sudo raspi-config` and setup stuff like timezone etc. --> IMPORTANT: THIS STEP HAS TO BE DONE!
* Select *Finish* in raspi-config, if the Raspberry does not ask to reboot, reboot it manually by entering `sudo reboot`
* Wait until its rebooted and againt SSH to your RPi or use keyboard/monitor
* Make sure your RPi has access to the internet
* Download the installation script by executing the following command:
* `wget https://raw.githubusercontent.com/peter9teufel/rasplooper/master/install_rasplooper.sh`
* Make the script executable with `sudo chmod +x install_rasplooper.sh`
* Run the installation with `sudo ./install_rasplooper.sh`
* Take a coffee.
* When installation is done, the RPi will reboot, initialize SD Card resizing to ensure the whole SD Card is used and then reboot again.
* That's it, you should be up and running.

## Bring media files to your RaspLooper ##
RaspLooper supports MP4 (h.264) out of the box, you can additionally obtain an MPEG2 license, again Google how to do that.

Copy your videos to a FAT32 USB Stick in a folder called *media*. This folder has to be on the root of your USB drive.
Connect the USB Stick to your RPi and boot it, it should detect the stick, copy your videos and as soon as it's done it will start playing your videos one after another in an endless loop.

That's it!

## Future enhancements ##
Honestly... I got a request for a simple player that can exactly do what it is able to do right now so I'm not sure if this player will see any feature updates soon. If you have an idea or a specific request for it, contact me. We'll see what I can do for you ;-)
