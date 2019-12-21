#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:03:16 2019

@author: sanjivshenoy
"""

#def intersection(List_of_lists): 
#    temp = set(List_of_lists[0])
#    for i in range(1,len(List_of_lists)):
#        temp = (temp & set(List_of_lists[i]))
#    return list(temp)
#
#L = [[1,2,3]]


def intersection(List_of_lists,Missing):
    ans = []
    for docs in List_of_lists[0]:
        ID = docs[0]
        cnt = 1
        word_cnts = [docs[2]]
        for j in range(1,len(List_of_lists)):
            for k in range(len(List_of_lists[j])):
                if(ID == List_of_lists[j][k][0]):
                    cnt+=1
                    word_cnts.append(List_of_lists[j][k][2])
        if(cnt == len(List_of_lists)):
            temp = [docs[0],docs[1],word_cnts,Missing]
            ans.append(temp)
    return ans

  
L1 = [[(1,2,3),(4,5,6),(7,8,9)],[(1,2,4),(4,5,7)],[(3,4,5),(4,5,7),(1,2,10)]]
ans = intersection(L1,['hello'])
print(ans)