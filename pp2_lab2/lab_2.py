# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:16:57 2020

@author: MARAT
"""

import os

path = r"C:\Users\MARAT\Desktop\KBTU\pp2\python\pp2_lab2"
os.chdir(path)

while (True):

    print ("Hello! It's the welcome text press \n 1: to change directory name \n "
           "2: list files of directory...")
    # 1: rename directory
    # 2: number of files
    # 3: amount of folders
    # 4: print all files of direcory
    # 5/6: create file, directory
    # 7: edit file
    command_id = int(input())
    if (command_id == 1):
        print ("Which directory you need to change:")
        directory_name = input()
        print ("Enter new name of the direcotry:")
        new_name = input()
        os.rename(directory_name, new_name)
    if (command_id == 2):
        files = os.listdir()
        print(files)
        print (len(files))
    if (command_id == 3):
        files = os.listdir()
        folder  = 0
        for x in files:
            if (os.path.isdir(x)):
                folder += 1
        print (folder)
    if (command_id == 4):
        files = os.listdir()
        print (files)
    if (command_id == 5):
        print ("Enter the name of the file:")
        file_name = input()
        open(file_name, "w+").close()
    if (command_id == 6):
        print ("Enter the name of the directory")
        d_name = input()
        os.mkdir(d_name)
    if (command_id == 7):
        print ("Enter name of the file")
        f_name = input()
        f = open(f_name, "a+")
        while (True):
            print ("print file editing option:")
            c = input()
            f = open(f_name, "a+")
            if (c == 'b'):
                print ("Enter the new name of the file")
                new_file_name = input()
                os.rename(f_name, new_file_name)
            if (c == 'a'):
                f.close()
                os.remove(f_name)
                break
            if (c == 'c'):
                print ("What to append to the file:")
                s = input()
                f.write(s)
                f.close()
            if (c == 'd'):
                break