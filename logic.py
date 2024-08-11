# app that sorts out downloads folder by user preferences

import os
import shutil
import multiprocessing


folders = {"Documents": ("doc", "docx", "edoc", "pdf", "asice", "txt", "odt", "rtf"),
           "Videos": ("mkv", "mp4", "m4v", "mkv", "avi", "mov"),
           "Presentations": ("ppt", "pptx", "ppsx"),
           "Audio": ("mp3", "wav", "wma"),
           "Applications": ("exe", "msi"),
           "Images": ("bmp", "img", "jpg", "png", "gif", "jpeg", "JPG"),
           "Archives": ("rar", "zip", "gz", "7z"),
           "Spreadsheets": ("xls", "xlsx", "csv")
           }
exc = []


def cleanup_folder(path, new_path, func, result, last=""):
    list = os.listdir(path)

    # creating new path for files
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    # writing down every file, splitting them into titles and extensions

    for file in list:
        title, ext = os.path.splitext(file)
        if ext:
            ext = ext[1:]
        else:
            shutil.copytree(path+'/'+file, new_path+'/'+file)
            continue
        print(title, ext)

    # checking if a file has a common extension, then allocating a folder for it

        if ext == last:
            pass
        else:
            directory = "Other"
            for key, value in folders.items():
                if ext in value:
                    directory = key
                    break

    # copying/moving files into new directiories
        try:
            if func:
                if os.path.exists(new_path+'/'+directory):
                    shutil.copy(path+'/'+file, new_path+'/'+directory+'/'+file)
                else:
                    os.makedirs(new_path+'/'+directory)
                    shutil.copy(path+'/'+file, new_path+'/'+directory+'/'+file)
                last = ext
            else:
                if os.path.exists(new_path+'/'+directory):
                    shutil.move(path+'/'+file, new_path+'/'+directory+'/'+file)
                else:
                    os.makedirs(new_path+'/'+directory)
                    shutil.move(path+'/'+file, new_path+'/'+directory+'/'+file)
                last = ext
        except PermissionError:
            exc.append(file)
            continue
    result.put(exc)
