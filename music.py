import eyed3, re, os

def musicSort(path):

    files_in_path = os.listdir(path)

    # raw_files = []
    clean_files = []

    for file in files_in_path:
        split_names = os.path.splitext(file)
        raw_extension = split_names[1]
        extension_name = raw_extension.lower()
    
        if extension_name == '.mp3':
            clean_files.append(file)


    # test remove site name in songs  
    for sound in clean_files:
        audio = eyed3.load(path + '/' + sound)

        if '|' in audio.tag.title:
            pattern = r'\|(.*)'
            replace = r''
            new = re.sub(pattern, replace,audio.tag.title)
            audio.tag.title = new
            audio.tag.save()
        # elif '-' in audio.tag.title:
        #     pattern = r'\-(.*)'
        #     replace = r''
        #     new = re.sub(pattern, replace,audio.tag.title)
        #     audio.tag.title = new
        #     audio.tag.save()
        
    print('Done')