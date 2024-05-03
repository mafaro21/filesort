import os, shutil
from moviepy.editor import *
from tqdm import tqdm 
import progressbar
import time

def orientationSort(vid_path):

    files_in_path = os.listdir(vid_path)

    folders = ['landscape','vertical']

    #create folders
    for loop in folders:
        if not os.path.exists(vid_path + loop):
            os.makedirs(vid_path + loop)

    raw_files = []
    clean_files = []

    class colors:
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'

    #separate files from folders ---- maybe use opencv
    for file in files_in_path:
        
        raw_files.append(file)
        split_names = os.path.splitext(file)
        extension_name = split_names[1]

        if not len(extension_name) == 0:
            clean_files.append(file)
        
    # clean_files_length = len(clean_files)
   
   
    #separate vertical from landscape and sort
    print('Reading video files', colors.WARNING+ '......'+ colors.ENDC )
    start_time = time.time()

    vertical_files = 0
    landscape_files = 0

    for vid in clean_files:
        video = VideoFileClip(vid_path + vid).subclip(0,4)

        width = video.w
        height = video.h 
        video.close()

        if width > height:
            if vid in files_in_path and not os.path.exists(vid_path + 'landscape/' + vid):
                landscape_files += 1
                shutil.move(vid_path + vid, vid_path + 'landscape/' + vid)
        else:
            if vid in files_in_path and not os.path.exists(vid_path + 'vertical/' + vid):
                shutil.move(vid_path + vid, vid_path + 'vertical/' + vid)
                vertical_files += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    #print message after sorting
    if vertical_files or landscape_files >= 1:
        print( vertical_files ,colors.OKGREEN + 'vertical files have been sorted'+ colors.ENDC)
        print( landscape_files ,colors.OKGREEN + 'landscape files have been sorted'+ colors.ENDC)
        print('Process took', minutes, "minute(s) &", seconds, 'seconds to sort')
    else:
        print(colors.FAIL + "There has been an error sorting." + colors.ENDC)