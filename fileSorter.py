import os, shutil

def SortExtension(path):
    # path = r"C:/Users/mafar/Pictures/4/"

    files_in_path = os.listdir(path)


    # --------------------SORTING BY EXTENSION----------------------------------
    extension_array = []
    clean_extension_array = []
    final_extension_array = []
    folder_names = []

    # separate filename from extension  
    for ext in files_in_path:
        split_names = os.path.splitext(ext)
        extension_name = split_names[1]
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

    if files >= 1:
        print(files , 'files have been sorted')
    else:
        print('There has been an error in sorting')

    # ---------BY FILE SIZE-----------------
    # test = os.stat(path + ext)
    #     final = test.st_size
    #     print(final)