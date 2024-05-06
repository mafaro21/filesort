import os, shutil, time, re
import eyed3

def SortExtension(path):

    files_in_path = os.listdir(path)

    # --------------------SORTING BY EXTENSION----------------------------------
    extension_array = []
    clean_extension_array = []
    final_extension_array = []
    folder_names = []

    class colors:
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        DONE = '\033[95m'

    # separate filename from extension  
    for ext in files_in_path:
        split_names = os.path.splitext(ext)
        raw_extension = split_names[1]
        extension_name = raw_extension.lower()
        extension_array.append(extension_name)
            
        count = -1
        # clean out folders from files  
        for clean_ext in extension_array:
            count = count + 1
            if len(clean_ext) == 0:
                del extension_array[count]
                continue
            # print(count)

            clean_extension_array.append(clean_ext)

            # clean out duplicates
            final_extension_array = list(set(clean_extension_array))

        #remove the . to create folder names
        for folder in final_extension_array:
            folder = folder + ' files'
            folder = folder.replace('.','')
            folder_names.append(folder)

        # create folders if not already there
        for loop in folder_names:
            if not os.path.exists(path + loop):
                os.makedirs(path + loop)

        files = 0
        start_time = time.time()
        # sort files by extension
        for file in files_in_path:
            for file_ext in extension_array:

                for folder in final_extension_array:
                    
                    if file_ext == folder:
                        folder = folder + ' files/'
                        folder = folder.replace('.','')

                        if file_ext in file and not os.path.exists(path + folder + file):
                            files += 1
                            shutil.move(path + file, path + folder + file)

        end_time = time.time()
        elapsed_time = end_time - start_time

        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        if files >= 1:
            print(files , colors.DONE + 'files have been sorted' + colors.ENDC)
            print(colors.OKGREEN + 'Process took', minutes, "minute(s) &", seconds, 'seconds to sort'+ colors.ENDC)
        else:
            print(colors.FAIL + 'There has been an error sorting' + colors.ENDC)