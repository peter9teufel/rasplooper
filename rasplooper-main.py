#! /usr/bin/env python

# libraries
import os, sys, subprocess, time, threading
import rasplooper

def shellquote(s):
    return "'" +  s.replace("'", "'\\''") + "'"

def startMediaPlayer():
    # set config and path for player and start it
    
    #rasplooper.setMediaPath(mediaPath)
    rasplooper.play()

def main():
    global mediaPath
    
    # default media path
    mediaPath = os.getcwd() + '/media/'
    #print "Media Path: " + mediaPath
    proc = subprocess.Popen(['tty'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = proc.communicate()
    print "Launching player..."

    # hide console text of local tty0 on hdmi
#    os.system("sudo sh -c \"TERM=linux setterm -foreground black -clear >/dev/pts/0\"")
    os.system("sudo sh -c \"TERM=linux setterm -foreground black -clear >/dev/tty0\"")

    startMediaPlayer()

    # simple CLI to modify and quit program when debugging
    print ""
    print ""
    print "Type command any time -->"
    print "-- \"quit\" to exit the program"
    print ""
    print ""

    running = True
    while running:
        cmd = raw_input("")
        if(cmd == "quit"):
            running = False
        else:
            print "Unknown command: ", cmd

    # bring back console text on tty0 on hdmi
    os.system("sudo sh -c \"TERM=linux setterm -foreground white -clear >/dev/pts/0\"")
    os.system("sudo sh -c \"TERM=linux setterm -foreground white -clear >/dev/tty0\"")

if __name__ == '__main__':
    print ""
    print ":::::::::::::::::::::::::::::::::::::::::::::::::"
    print "::::::::::::: WELCOME TO RASPLOOPER :::::::::::::"
    print ":::::::::::::::::::::::::::::::::::::::::::::::::"
    print ""
    main()
