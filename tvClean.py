import os, re, time

def tvClean(path):
    # path = r'C:/Users/mafar/Videos/S01' 

    files_in_path = os.listdir(path)

    quality = ['720p', '1080p']

    class colors:
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        DONE = '\033[95m'

    start_time = time.time()
    files_sorted = 0

    for file in files_in_path:
        name = os.path.splitext(file)
        split = name[0]

        separated_name = split.replace('.', ' ')
        # print(name)
        # t = '720p'
        for type in quality:
            if type in separated_name:
                pattern = rf'(?<={type}).*'
                replace = r''
                clean_name = re.sub(pattern, replace, separated_name)
            #    print(new) 
            
        final_name = clean_name + name[1]
        # print(final_name)

        old_full_path = path + "/" + file
        full_path = path + "/" + final_name

        os.rename(old_full_path, full_path)
        files_sorted += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    if files_sorted >= 1:
        print( files_sorted ,colors.DONE + 'files have been sorted'+ colors.ENDC)
        print(colors.OKGREEN + 'Process took', minutes, "minute(s) &", seconds, 'seconds to sort'+ colors.ENDC)
    else:
        print(colors.FAIL + "There has been an error sorting." + colors.ENDC)


