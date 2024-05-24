import os, shutil
from moviepy.editor import *
from tqdm import tqdm 
import progressbar
import time

def orientationSort(vid_path):

    files_in_path = os.listdir(vid_path)

    folders = ['landscape','vertical']

    file_types = ['.mp4','.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.3gp', '.3g2', '.mpeg', '.ogg', '.divx', '.xvid', '.h.264','.h.264' ]

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
        ENDC = '\033[0m'
        DONE = '\033[95m'

    #separate files from folders, exclude non video files ---- maybe use opencv
    for type in file_types:
        
        if type  in file_types:
            for file in files_in_path:

                raw_files.append(file)
                split_names = os.path.splitext(file)
                raw_extension = split_names[1]
                extension_name = raw_extension.lower()

                if not len(extension_name) == 0:
                    if extension_name == type:
                        clean_files.append(file)
        else:
            break
        
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
                print('Duplicate File Found -->', vid)
        else:
            if vid in files_in_path and not os.path.exists(vid_path + 'vertical/' + vid):
                shutil.move(vid_path + vid, vid_path + 'vertical/' + vid)
                vertical_files += 1
            else:
                print('Duplicate File Found -->', vid)

    end_time = time.time()
    elapsed_time = end_time - start_time

    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    #print message after sorting
    if vertical_files or landscape_files >= 1:
        print( vertical_files ,colors.DONE + 'vertical files have been sorted'+ colors.ENDC)
        print( landscape_files ,colors.DONE + 'landscape files have been sorted'+ colors.ENDC)
        print(colors.OKGREEN + 'Process took', minutes, "minute(s) &", seconds, 'seconds to sort'+ colors.ENDC)
    else:
        print(colors.FAIL + "There has been an error sorting." + colors.ENDC)