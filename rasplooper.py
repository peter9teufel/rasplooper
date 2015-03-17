#! /usr/bin/env python

import os, platform, threading, time, subprocess, re

# filetypes
SUPPORTED_IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG')
SUPPORTED_VIDEO_EXTENSIONS = ('.mp4', '.m4v', '.mpeg', '.mpg', '.mpeg1', '.mpeg4', '.avi')

# state variables and paths
PLAYER_STOPPED = 0x00
PLAYER_STARTED = 0x01
playerState = PLAYER_STOPPED
cwd = os.getcwd()
mediaPath = cwd + '/media/'
mp_thread = None
videoPlaying = False

class MediaPlayer(threading.Thread):
    def __init__(self):
        global playerState
        self.mediaPath = os.getcwd() + '/media/'
        self.runevent = threading.Event()
        playerState = PLAYER_STOPPED
        threading.Thread.__init__(self, name="MediaPlayer_Thread")

    def run(self):
        global playerState, identifyFlag
        while True:
            self.processMediaFiles()

    def processVideosOnce(self):
        global playerState
        files = self.allVideos()
        files.sort()
        for file in files:
            self.playVideo(file)

    def videoLoop(self):
        videos = self.allVideos()
        #if len(videos) == 1:
        #    self.singleVideoLoop(videos[0])
        #else:
        while playerState == PLAYER_STARTED:
            self.processVideosOnce()

    def processVideosOnly(self):
        global playerState
        print "Processing only videos."
        self.videoLoop()

    def playVideo(self,file):
        global playerState
        global videoPlaying
        # process video file -> omxplay will block until its done
        #print "Status PLAYER_STARTED: ", playerState == PLAYER_STARTED
        if playerState == PLAYER_STARTED:
            fullPath = os.path.join(self.mediaPath, file)
            videoPlaying = True
            subprocess.call([cwd + '/scripts/omxplay.sh', os.path.join(self.mediaPath, file)])
            videoPlaying = False

    def allVideos(self):
        videos = []
        for file in os.listdir(self.mediaPath):
            if file.endswith((SUPPORTED_VIDEO_EXTENSIONS)):
                videos.append(file)
        return videos

    def processMediaFiles(self):
        global playerState
        self.processVideosOnly()

        # set player state to stopped as processing is done at this point
        playerState = PLAYER_STOPPED

def play():
    global playerState
    playerState = PLAYER_STARTED
    global mp_thread

    # media file processing in separate thread
    if not mp_thread.isAlive():
        mp_thread.start()
    mp_thread.runevent.set()
    print "Mediaplayer running in thread: ", mp_thread.name


def main():
    global cwd, mp_thread, playerState
    print "PLAYER CWD: " + cwd
    if not mp_thread:
        mp_thread = MediaPlayer()
        mp_thread.daemon = True
    playerState = PLAYER_STOPPED
    mp_thread.start()

main()
