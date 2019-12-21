import math
import json

#Calculating IDF
invertedIndex={}
mylist=[]  #contains list of terms
scores=dict()  # has scores corresponding to each document updated given a query
length_eachdoc_vector=dict()  # has normalization factors of each document when seen as a vector
idf=dict() 
            
            
data=open('documents.txt')
# termlist=open('example.txt')
# for eachline in termlist:
#     (term, discard)=eachline.split('<',1)
#     invertedIndex[term]=[]
#     mylist.append(term)

f=open("words.txt", "r")

mylist = []
if f.mode == 'r':
    contents = f.read()
    mylist = contents.split(',')
    del[mylist[0]]
    mylist.insert(0,'i')
    mylist[len(mylist)-1] = 'kad'

# print(mylist)

f.close()

for term in mylist:
    invertedIndex[term] = []
    
maxnum=len(mylist)
doc_freq_t=[0 for i in range(maxnum)]

i=0
for eachline in data:
    i+=1
    (docID, discard, terms)=eachline.split(',', 2)
    scores[docID]=0
    length_eachdoc_vector[docID]=0
    
    while not terms.find(':')==-1:
        if not terms.find(',')==-1:
            (t, terms)=terms.split(',', 1)
        else:
            t=terms
            terms=""
        (term_num, freq)=t.split(':',1)
        term_num=int(term_num)
        freq=float(freq)
        
        # updating the normalization constant of each document vector
        present_len = length_eachdoc_vector[docID]
        length_eachdoc_vector[docID]= math.sqrt(math.pow(present_len,2) + math.pow(freq,2))
        
        # adding this docID to corresponding term's posting list in the Inverted Index
        
        if term_num<maxnum:
            invertedIndex[mylist[term_num-1]].append([docID, freq])
            doc_freq_t[term_num-1]=len(invertedIndex[mylist[term_num-1]]) #updating document frequency
                                                                          #for curr term

total_num_doc=i

#prints the idf values of all the terms (this block of code is to be removed) 
print(total_num_doc)
print("Here is the inverse documnet frequency for each term:")
for word in invertedIndex:
    docfreq=len(invertedIndex[word])
    if docfreq!=0:
        idf[word]=(10*math.log10(total_num_doc/len(invertedIndex[word])))
    else:
        idf[word]=0


json = json.dumps(idf)
f = open("idf.json","w")
f.write(json)
f.close()

