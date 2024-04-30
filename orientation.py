import os, shutil
from moviepy.editor import *

def orientationSort(vid_path):
    # vid_path = 'C:/Users/mafar/Videos/dev/DB/'

    files_in_path = os.listdir(vid_path)

    folders = ['landscape','vertical']

    raw_files = []
    clean_files = []
    landscape = []
    vertical = []

    count = 0
    for file in files_in_path:
        
        raw_files.append(file)
        split_names = os.path.splitext(file)
        extension_name = split_names[1]
        # print(count)

        if not len(extension_name) == 0:
            clean_files.append(file)
        

    #separate vertical from landscape
    for vid in clean_files:
        video = VideoFileClip(vid_path + vid).subclip(0,10)

        width = video.w
        height = video.h 
        calc_width = width * (9/16)

        if calc_width >= 640:
            landscape.append(vid)
        else:
            vertical.append(vid)

        video.close()

    #create folders
    for loop in folders:
        if not os.path.exists(vid_path + loop):
            os.makedirs(vid_path + loop)

    vertical_files = 0
    landscape_files = 0

    # sort files
    for vid in vertical:
        if vid in files_in_path and not os.path.exists(vid_path + 'vertical/' + vid):
            vertical_files += 1
            shutil.move(vid_path + vid, vid_path + 'vertical/' + vid)

    for vid in landscape:
        if vid in files_in_path and not os.path.exists(vid_path + 'landscape/' + vid):
            landscape_files += 1
            shutil.move(vid_path + vid, vid_path + 'landscape/' + vid)

    if vertical_files or landscape_files >= 1:
        print(vertical_files, 'vertical files have been sorted')
        print(landscape_files, 'landscape files have been sorted')
    else:
        print('There has been an error sorting')