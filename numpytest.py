import numpy as np


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

documents = np.zeros((5000,210519))
doc_id = {}

if f2.mode == 'r':
    contents = f2.read()
    documents_string = contents.strip().split()
    for s in documents_string:
        t = s.split(',')
        doc_id1 = t[0]
        doc_id2 = t[1]
        del(t[0])
        del(t[0])
        l = (doc_id1, doc_id2)
        doc_id[s] = l
        for i in t:
            w_c = i.split(':')
            documents[int(w_c[0])-1][s] = 1
 
f2.close()

print(documents)
