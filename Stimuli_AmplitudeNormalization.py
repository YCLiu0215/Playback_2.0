# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:20:30 2024

@author: Liu
"""
from pydub import AudioSegment
import os
import numpy as np

#export folder name
Folder = 'Test'
#Folder for putting song files
dir_path_song = r'C:\Users\Liu\Dropbox (OIST)\Data\Yoko Unit\Ephys\Stimuli\Song_temp'
#Folder for putting label files (make sure the file name is the same as the song file)
dir_path_label = r'C:\Users\Liu\Dropbox (OIST)\Data\Yoko Unit\Ephys\Stimuli\Label_temp'
#Directory of exportation
dir_path_export = r'C:\Users\Liu\Dropbox (OIST)\Data\Yoko Unit\Ephys\Stimuli\\'+Folder

file = os.listdir(dir_path_song)

#Tatget amplitude
target_amp = -20
#Duration of the file (sec.), the code will append silence to make it the determined duration.
file_duration = 10




def SongAmpNorm(file):
    
    #open wav file by Audiosegment
    os.chdir(dir_path_song)
    song = AudioSegment.from_wav(file)
    os.chdir(dir_path_label)
    Labels = np.loadtxt(file[:-4]+'.txt')*1000      
    os.chdir(dir_path_export)
    #Slice audio into syllables and gaps
    Syllables = []
    Gaps = []
    for i in range (len(Labels)):
        Syllables.append(song[Labels[i,0]:Labels[i,1]])
        if i < int(len(Labels))-1:
            Gaps.append(song[Labels[i,1]:Labels[i+1,0]])
        else:
            pass
    
    #Measure the avg. volume of syllables
    song_syl = Syllables[0]
    for i in range (1,len(Syllables)):
        song_syl = song_syl+Syllables[i]
    
    original_amp = song_syl.dBFS
    tune = target_amp-original_amp
    
      
    
    song_norm = song + tune
    Silence = AudioSegment.silent(duration=file_duration*1000-len(song_norm), frame_rate=32000)
    song_norm = song_norm + Silence
    
    song_norm.export(file[:-4]+'_normalized.wav', format="wav")

if __name__=="__main__":
    for i in range (len(file)):
        SongAmpNorm(file[i])