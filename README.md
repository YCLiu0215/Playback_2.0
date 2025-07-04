1. Stimuli_AmplitudeNormalization.py - simply putting song files and label files in different folders, you can batchly normalize the amplitude and append silence to make every file the same duration. /n
   **Important parameters**
   Folder: the name of the folder for output the normalized song files.
   dir_path_song: the directory of song files (.wav).
   dir_path_label: the directory of label files (.txt) exported from avisoft (you dont need to give the name to the labels at all, the code only need the start and end time of each labeled syllables).
   dir_path_export: the directory of the output folder.
   target_amp: the amplitude you are normalizing it to. Although the number is negative, but the bigger the number the louder the sound (ex. -10 is louder than -20).
   file_duration: the target duration of the files. the code will automatically add silence to the end of the song file, and make it exactly the duration you ask for.
2. SugiyamaUnit_Playback_ver2.0.py - Simply putting all the songfiles you want to play in a folder and you can randomly play those songs, and you will get a log sheet of playback timing and all the files you have played.
   (I have another version with the scheduled playback function, I am happy to provide that upon request)
   **Important parameters**
   frequency=32000: please make sure the sampling rate is correct. Our song files usually have a sampling rate of 32k Hz.
   dir_song: the directory to the folder of the song files you are going to playback.
   Log_sheet_name: the name of the excel logsheet.
   dir_log: the directory you want the excel logsheet to be exported to.
   T: the total duration of the playback (sec.) (ex. if an hour of playback should be 3600).
   d: the duration of the song files (sec.), the code is supposed to playback time for this long before it cut the song off and play the next one. The song file duration can be shorter than this but not over this, otherwise it will be cut off.
   avg: average interval.
   std: the variation of the interval (ex. avg = 5, std = 5 means the intervals could be 5 +- 5 sec.).
   preWait: how many seconds you want the code to wait until it starts playback.
