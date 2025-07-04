# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:23:23 2020

@author: Liu
"""
import subprocess
import pygame as pg
import pyautogui
import random
import time
import pandas as pd
import os
from datetime import datetime
#the sampling rate of song playback, need to be set according to song files#
pg.mixer.init(frequency=32000, size=-16,channels=2, buffer=4096)
#Load sound files

#directory of the folder for song files
dir_song = r'C:\Users\Liu\Dropbox (OIST)\Data\Yoko Unit\Ephys\Stimuli\O799'

songs = os.listdir(dir_song)


channel0 = pg.mixer.Channel(0)

Log_sheet_name = 'Playback_20240603_test.xlsx'
#directory for log sheet exportation
dir_log = r'C:\Users\Liu\Dropbox (OIST)\Data\Yoko Unit\python'


#set the duration of song stimulation
# T, total playback time; d, duration of each playback; avg, avg of random interval; std, the range of interval
T = 3600
d = 10
avg = 5
std = 5

times = int (T / (d + avg))

preWait = 0






### DN = time.strptime(str(datetime.now())[0:19],'%Y-%m-%d %H:%M:%S')


Playback = []
def Play():
    os.chdir(dir_song)
    r = random.randint (0,len(songs)-1)
    sound = pg.mixer.Sound(songs[r])     
    Playback.append(songs[r][:-4])
    channel0.play(sound)
    time.sleep(d)


start_time = time.time
def t():
    return time.time()-start_time


N = 60

def NoLock(a):
    pyautogui.press('capslock')
    time.sleep(0.5)
    pyautogui.press('capslock')
    print('waiting...')
    time.sleep(a)


# get a list of pseudo-random numbers

def get_r():
    global r
    r = []
    for i in range (int(times/2)):
        Y = random.randint (-std, std)
        r.append(avg+Y)
        r.append(avg-Y)
    random.shuffle(r)





Play_time = []
def main():
    
    print('Wait for '+str(preWait)+' min')
    for i in range(preWait):
        NoLock(N)

    P = 0
    global start_time
    start_time = time.time()
    for i in range (times):
        try:
            P += 1
            Play_time.append(t())
            Play()
            time.sleep(r[i])
    #you can interrupt the playback using ctrl+c
        except KeyboardInterrupt:
            print ('Playback has been interrupted')
            break
    
    End_text = 'Song files have been played for '+ str(P) + ' times, and last for ' + str(t()) + ' seconds'
    print (End_text)

   





    
os.chdir(dir_log)
if os.path.exists(Log_sheet_name) == False:
    writer = pd.ExcelWriter(Log_sheet_name, engine='xlsxwriter')
    Playback = []
    Play_time = []
    get_r()
    main()
    
    os.chdir(dir_log)
    df = pd.DataFrame([Play_time, Playback, r],
             index =['Time', 'Song', 'Interval'])
    df_T = df.T
    df_T.to_excel(writer)
    writer.close()
else:
    print ('File has already existed, do you want to proceed on? [y/n]')
    D = input()
    if D == 'y':
        try:
            myfile = open(Log_sheet_name, "r+") # or "a+", whatever you need
        except IOError:
            print ('Could not open file! Please close Excel!')

        with myfile:
            writer = pd.ExcelWriter(Log_sheet_name, engine='xlsxwriter')
            Playback = []
            Play_time = []
            get_r()
            main()
            
            os.chdir(dir_log)
            df = pd.DataFrame([Play_time, Playback, r],
                    index =['Time', 'Song', 'Interval'])
            df_T = df.T
            df_T.to_excel(writer)
            writer.close()
    if D == 'n':
        print ('The process has been interrupted')
    else:
        pass
  




