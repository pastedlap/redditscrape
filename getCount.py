#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:32:42 2018

@author: ayx
"""
import glob
def count_threads():
    fl_names=glob.glob("./data/comments/*.txt")
    cnter=0
    for fl_name in fl_names:
        with open(fl_name) as f:
            contents = f.read()
            cnt = contents.count("@@@THREAD@@@")   
            cnter+=cnt
    print('Total thread count is ' + str(cnter))
    return cnter
def count_links():
    fl_names=glob.glob("./data/links/*.txt")
    cnter=0
    for fl_name in fl_names:
        with open(fl_name) as f:
            contents = f.read()
            cnt = contents.count("https://")   
            cnter+=cnt
    print('Total links count is ' + str(cnter))
    return cnter

count_comments()
count_links()