#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-

import os
import sys
import re


class find_keywords():
    def __init__(self):
        keywords = ""
        last_keywords = ""

    def open_file(self, file_url, mode):
        filefp = open(file_url, mode)


    def searchkey(self, key, key_and):
        pass


#### search keys  ####
    def find_file_by_pattern(pattern='.*', base="bbklog", circle=True):
        '''查找给定文件夹下面所有 '''
        re_file = re.compile(pattern)
    	if base == ".":
    		base = os.getcwd()

    	final_file_list = []
    	print base
    	cur_list = os.listdir(base)
    	for item in cur_list:
    		if item == ".svn" or item == ".repo" or item ==".git":
    			continue

    		full_path = os.path.join(base, item)
    		if full_path.endswith(".doc") or \
    			full_path.endswith(".bmp") or \
    			full_path.endswith(".wpt") or \
    			full_path.endswith(".dot"):
    			continue

    		# print full_path
    		bfile = os.path.isfile(item)
    		if os.path.isfile(full_path):
    			if re_file.search(full_path):
    				final_file_list.append(full_path)
    		else:
    			final_file_list += find_file_by_pattern(pattern, full_path)
    	return final_file_list


####  end search keys ####


