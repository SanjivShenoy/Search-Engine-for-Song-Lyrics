# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:10:40 2019
@author: Sanjiv
@author: Manish
"""

#Importing useful libraries
import os
import math
import json

from itertools import combinations 


#Store all unique words in all songs in a list L
#Used to get the word if the word index is known
f=open("words.txt", "r")

L = []
if f.mode == 'r':
    contents = f.read()
    L = contents.split(',')
    del[L[0]]
    L.insert(0,'i')
    L[len(L)-1] = 'kad'

f.close()


with open('doc_dict.json', 'r') as f2:
    documents = json.load(f2)


'''
Increasing time instead of decreasing it.
'''
# with open('word_hash.json', 'r') as f3:
    # word_hash = json.load(f3)


print("Speed Test Completed")