#!/usr/bin/env python3

from pccold.videodownload import downloadVideo, ReturnCodeObserverThread, SleepKillerThread

print('PcCold with DKZ download video')
ReturnCodeObserverThread.main = downloadVideo
SleepKillerThread.main = downloadVideo
downloadVideo()
