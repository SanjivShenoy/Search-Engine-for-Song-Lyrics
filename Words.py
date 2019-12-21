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

# Documents is a dictionary with key as doc_ID mapping 
# to a list in which each item contains
# the doc_ID, mxn_music_ID, and a dictionary 
# of words in the document mapping to their counts. 
with open('doc_dict.json', 'r') as f2:
    documents = json.load(f2)  


#word_hash is a dictionary storing the inverted index
#It also contains the term frequency of the word in each document.
word_hash = {}

for doc in documents:
    for wd in documents[doc][2]:
        if wd not in word_hash:
            word_hash[wd] = []
            word_hash[wd].append((documents[doc][0],documents[doc][1],documents[doc][2][wd]))
        else:
            word_hash[wd].append((documents[doc][0],documents[doc][1],documents[doc][2][wd]))

#Input - Lists of documents
#Output - Intersection of the lists
def intersection2(List_of_lists):
    if (len(List_of_lists) == 0):
        return ([])
    temp = set(List_of_lists[0])
    for i in range(1,len(List_of_lists)):
        temp = (temp & set(List_of_lists[i]))
    return list(temp)

#Getting the inverse document frequencies of all words
with open('idf.json', 'r') as f:
    idf = json.load(f)


# Input - selection of query words as a list
# Returns the ranked list of documents  

def minSelect(query):
    List_of_list_of_documents = []
    
    for i in range(len(query)):
        if query[i] in word_hash.keys():
            List_of_list_of_documents.append(word_hash[query[i]])
    
    
    #Code to just take out the Doc IDs. 
    L = []
    for i in range(len(List_of_list_of_documents)):
        t = []
        for j in range(len(List_of_list_of_documents[i])):
            t.append(List_of_list_of_documents[i][j][0])
        L.append(t)
    
    #Intersection of the doc_IDs for different words
    ans = intersection2(L)
    # print(len(ans))
    
    #List containing the document IDs and the list of words with tf in doc
    doc_query_wdlist = []
    for doc_id in ans:
        query_wdlist =[]
        for wd in query:
            if wd in documents[doc_id][2].keys():
                query_wdlist.append([wd, documents[doc_id][2][wd]])
        doc_query_wdlist.append([documents[doc_id][0], documents[doc_id][1], query_wdlist])

    # Sorts the documents in decreasing values of minimum word count(tf)
    Top = []
    for i in doc_query_wdlist:
        l = []
        for j in i[2]:
            l.append(j[1])
        l.sort()
        Top.append( (l, i[0], i[1]) )

    Top.sort(reverse = True)

    return Top

#Import function to stem query using Porter's Algorithm
from lyricsToBow import lyrics_to_bow

#Infinite loop to accept queries
while(1):
    lyrics = input("Enter your Query (type QUIT to exit): ")
    if lyrics == "QUIT" :
        break

    #Stem the query and return list of query words
    query = lyrics_to_bow(lyrics)

    #List of IDF values of all terms
    IDF_values = []
    for term in query:
        if term in idf.keys():
            IDF_values.append((idf[term],term))

    IDF_values.sort(reverse=True)


    # Storing all word combinations of query words
    Combo_L = []

    for r in range(len(IDF_values),0,-1):
        combo_r = list(combinations(IDF_values, r))
        combo_r.sort(reverse = True)
        Combo_L.append(combo_r)
    
    # Printing overall top 10 documents
    rem = 10
    s = set()
    for combo in Combo_L:
        if rem <= 0:
            break
        for i in combo:
            if rem <= 0:
                break
            sub_query = []
            for j in i:
                sub_query.append(j[1]);
            Top = minSelect(sub_query)
            val = min(len(Top),rem)
            for k in range(val):
                if(Top[k][1] not in s):
                    print("Doc_ID =", end=' ')
                    print(Top[k][1]) #print(Top[k][1], end='  ')
                    s.add(Top[k][1])
                    # print("mxm_ID =", end=' ')
                    # print(Top[k][2])
            rem = (10 - len(s))








        