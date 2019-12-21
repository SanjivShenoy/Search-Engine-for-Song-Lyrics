import os
import math
os.getcwd()
# os.chdir('C:\\Users\\jtuli\\Desktop\\IR assignment 1')
os.getcwd()


# function that returns top 10 document ID's in decreasing order of relevance

def funct (listt):
    return listt[1]
    
def top10_final (query):
    listofscores=[] #document ID and corresponding score of top 10 docs
    top10_list=[] #contains top 10 document IDs without scores
    
    for eachterm in query:
        if eachterm in invertedIndex:
            for doc_and_freq in invertedIndex[eachterm]:
                docID=doc_and_freq[0]
                termfreq=doc_and_freq[1]
                scores[docID]=scores[docID]+termfreq*idf[eachterm]
        
        else:
            continue
    for each_doc in scores:
        if scores[each_doc] != 0:
            scores[each_doc]= scores[each_doc]/length_eachdoc_vector[each_doc]
            listofscores.append([each_doc, scores[each_doc]])
    print(len(listofscores))
    
    sorted(listofscores, key=funct, reverse=True)
    k=0
    for doc_score_pair in listofscores:
        k+=1
        top10_list.append(doc_score_pair[0])
        if k==10:
            break
            
    return top10_list


invertedIndex={}
mylist=[]  #contains list of terms
scores=dict()  # has scores corresponding to each document updated given a query
length_eachdoc_vector=dict()  # has normalization factors of each document when seen as a vector
idf=dict() 
            
            
data=open('documents.txt')
# data=open('example1.txt')
# termlist=open('example.txt')
# for eachline in termlist:
#     (term, discard)=eachline.split('<',1)
#     invertedIndex[term]=[]
#     mylist.append(term)

f=open("words.txt", "r")

if f.mode == 'r':
    contents = f.read()
    mylist = contents.split(',')
    del[mylist[0]]
    mylist.insert(0,'i')
    mylist[len(mylist)-1] = 'kad'

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


#Import function to stem query using Porter's Algorithm
from lyricsToBow import lyrics_to_bow

#prints the idf values of all the terms (this block of code is to be removed) 
print(total_num_doc)
print("Here is the inverse documnet frequency for each term:")
for word in invertedIndex:
    docfreq=len(invertedIndex[word])
    if docfreq!=0:
        idf[word]=(10*math.log10(total_num_doc/len(invertedIndex[word])))
    else:
        idf[word]=0

lyrics = input("Enter your Query (type QUIT to exit): ")

# query="help che togeth cold becaus "
query = lyrics_to_bow(lyrics)
answer=top10_final(query)


print("The top 10 documents are:")
for doc in answer:
    print(doc)
            
data.close()
# termlist.close()
