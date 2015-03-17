#! /usr/bin/env python

import os, sys, subprocess, time, shutil, threading, random
import urllib2

# filetypes
SUPPORTED_IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG')
SUPPORTED_VIDEO_EXTENSIONS = ('.mp4', '.m4v', '.mpeg', '.mpg', '.mpeg1', '.mpeg4', '.avi')

# paths
ROOT_PATH = "/home/pi/rasplooper/"
MEDIA_PATH = ROOT_PATH + "/media"
USB_PATH = "/media/usb0/"
USB_MEDIA_PATH = USB_PATH + 'media'

def UsbDrivePresent():
    proc = subprocess.Popen(["ls /dev | grep 'sda'"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if 'sda' in out:
        return True
    else:
        return False

def MediaFilesPresent():
    # check if usb contains kiosk directory
    if os.path.isdir(USB_MEDIA_PATH):
        print "USB directory present"
        return True

def CopyMediaFiles():
    print "Copying files from USB to RaspLooper Player"
    clear = True
    if clear:
        # delete previous files from player
        shutil.rmtree(MEDIA_PATH)
        if not os.path.isdir(MEDIA_PATH):
            os.mkdir(MEDIA_PATH)
    for file in os.listdir(USB_MEDIA_PATH):
        if not file.startswith('.'):
            if file.endswith((SUPPORTED_VIDEO_EXTENSIONS)):
                vidEnabled = 1
                print "Copy video file: ", file
                size = (os.stat(USB_MEDIA_PATH + '/' + file).st_size)
                size /= 1024
                size /= 1024
                fileSize = str(size) + 'MB'
                print "Size: ", fileSize
                print "Please wait..."
                srcFile = USB_MEDIA_PATH + '/' + file
                dstFile = MEDIA_PATH + '/' + file
                shutil.copyfile(srcFile, dstFile)

    print "Media files copied to player successfully!"
    print "Configuring playback settings for your new media files..."
    print "Done!"

# Main Method
def StartupRoutine():
    if not os.path.isdir(MEDIA_PATH):
        os.mkdir(MEDIA_PATH)
    if UsbDrivePresent():
        print "USB device present"
        if MediaFilesPresent():
            print "Media files found on USB device"
            CopyMediaFiles()
        else:
            print "No media files found on USB device"
    print ""
    print "Startup routine finished, starting RaspLooper Player..."
    print "Bye bye..."
    print ""

    time.sleep(2)

    os.system("sudo python rasplooper-main.py > /dev/null")


StartupRoutine()