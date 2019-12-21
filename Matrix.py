import math
import json

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

temp = []
for i in range(len(L)):
	temp.append(0)

documents = {}

if f2.mode == 'r':
    contents = f2.read()
    documents_string = contents.strip().split()
    for s in documents_string:
        t = s.split(',')
        doc_id1 = t[0]
        doc_id2 = t[1]

