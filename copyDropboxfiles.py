# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:34:47 2014

@author: wgillis
"""

import os, shutil

dropbox_directory = 'C:/Users/wgillis/Dropbox/birdsong papers'
google_drive_directory = 'C:/Users/wgillis/Google Drive/birdsong papers'

def copyFilesRecursively(directory, to):
    src_files = os.listdir(directory)
    end_files = find_all_files(to)
    for file_name in src_files:
        fullname = os.path.join(directory, file_name)
        if os.path.isfile(fullname):
            if file_name not in end_files:                  
                try:
                    shutil.copy(fullname, to)
                except:
                    pass
        elif os.path.isdir(fullname):
            copyFilesRecursively(fullname, os.path.join(to, file_name))
            
def find_all_files(directory):
    files = []
    def file_recursive(dire):
        for obj in os.listdir(dire):
            full = os.path.join(dire, obj)
            if os.path.isfile(full):
                files.append(obj)
            elif os.path.isdir(full):
                file_recursive(full)
    file_recursive(directory)
    return files

if __name__=='__main__':
    copyFilesRecursively(dropbox_directory, google_drive_directory)