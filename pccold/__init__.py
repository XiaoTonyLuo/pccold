from pccold.pccold import main
from pccold.videodownload import downloadVideo, download3DaysVideo
from pccold.danmu import Danmu
from pccold.tools import ReturnCodeObserverThread, SleepKillerThread

'''
test
'''

"""
dapanpanpanji's commit 
"""
i = 0
while True:
    i += 1
    if i % 10 == 1:
        print(i)

    if i >= 23:
        break
