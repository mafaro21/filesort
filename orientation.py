import os, shutil
from moviepy.editor import *
# from tqdm import tqdm 
import progressbar

def orientationSort(vid_path):

    files_in_path = os.listdir(vid_path)

    folders = ['landscape','vertical']

    raw_files = []
    clean_files = []
    landscape = []
    vertical = []

    class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    #separate files from folders ---- maybe use opencv
    for file in files_in_path:
        
        raw_files.append(file)
        split_names = os.path.splitext(file)
        extension_name = split_names[1]

        if not len(extension_name) == 0:
            clean_files.append(file)
        
    clean_files_length = len(clean_files)
   
   
    #separate vertical from landscape
    print('Reading video files', colors.WARNING+ '......'+ colors.ENDC )

    # for i in tqdm(range(clean_files_length), colour='green', bar_format='{l_bar}{bar}| {n}/{total} |{elapsed}/{remaining}'):
        # time.sleep(0.1) 

    # for i in progressbar.progressbar(range(clean_files_length)):
        
    for vid in clean_files:
        video = VideoFileClip(vid_path + vid).subclip(0,4)

        width = video.w
        height = video.h 
        # calc_width = width * (9/16)
        video.close()

        if width > height:
            landscape.append(vid)
        else:
            vertical.append(vid)


    #create folders
    for loop in folders:
        if not os.path.exists(vid_path + loop):
            print('Creating folder')
            os.makedirs(vid_path + loop)

    vertical_files = 0
    landscape_files = 0

    vert_length = len(vertical)
    land_length = len(landscape)

    # sort files
    if vert_length > 0:
        for vid in vertical:
            if vid in files_in_path and not os.path.exists(vid_path + 'vertical/' + vid):
                shutil.move(vid_path + vid, vid_path + 'vertical/' + vid)
                vertical_files += 1
                    
    if land_length > 0:
        for vid in landscape:
            if vid in files_in_path and not os.path.exists(vid_path + 'landscape/' + vid):
                landscape_files += 1
                shutil.move(vid_path + vid, vid_path + 'landscape/' + vid)

    #print message after sorting
    if vertical_files or landscape_files >= 1:
        print( vertical_files ,colors.OKGREEN + 'vertical files have been sorted'+ colors.ENDC)
        print( landscape_files ,colors.OKGREEN + 'landscape files have been sorted'+ colors.ENDC)
    else:
        print(colors.FAIL + "There has been an error sorting." + colors.ENDC)