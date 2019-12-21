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

f2 = open("documents.txt", "r")


#Creating a list of words and their respective frequencies for each document.
#It is a dictionary with key as doc_ID mapping to a list in which each item contains
#the doc_ID, mxn_music_ID, and a dictionary of words mapping to their counts.  
documents = {}

if f2.mode == 'r':
    contents = f2.read()
    documents_string = contents.strip().split()
    for s in documents_string:
        t = s.split(',')
        doc_id1 = t[0]
        doc_id2 = t[1]
        l = []
        l.append(t[0])
        l.append(t[1])
        words = {}
        del(t[0])
        del(t[0])
        for i in t:
            w_c = i.split(':')
            words[L[int(w_c[0])-1]] = int(w_c[1])
        l.append(words)
        documents[doc_id1] = l
 
f2.close()

print(len(L))
print(len(documents))

# json = json.dumps(documents)
# f = open("doc_dict.json","w")
# f.write(json)
# f.close()

# print("Dictionary added to file")

# word_hash = {}

# for doc in documents:
#     for wd in documents[doc][2]:
#         if wd not in word_hash:
#             word_hash[wd] = []
#             word_hash[wd].append((documents[doc][0],documents[doc][1],documents[doc][2][wd]))
#         else:
#             word_hash[wd].append((documents[doc][0],documents[doc][1],documents[doc][2][wd]))

# json = json.dumps(word_hash)
# f3 = open("word_hash.json","w")
# f3.write(json)
# f3.close()

# print("Dictionary added to file")

