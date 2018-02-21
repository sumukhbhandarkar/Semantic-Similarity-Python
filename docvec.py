import re, numpy
from numpy import dot
from numpy.linalg import norm
from nltk.corpus import stopwords
from numpy import zeros
import porter
#from porter import PorterStemmer
from nltk.stem import PorterStemmer
splitter=re.compile ( "[a-z\-']+", re.I )
stemmer=PorterStemmer()

stop = set(stopwords.words('english'))
stop_words = list(stop)

all_words=dict()
def add_word():
        w=word.lower()
        if w not in stop_words:
                ws=stemmer.stem(w,0,len(w)-1)
                all_words.setdefault(ws,0)
                all_words[ws] += 1

key_idx=dict()
keys=all_words.keys()
keys.sort()
for i in range(len(keys)):
        key_idx[keys[i]] = (i,all_words[keys[i]])
del keys
del all_words

def doc_vec(doc):
        v=zeros(len(key_idx))
        for word in splitter.findall(doc):
                keydata=key_idx.get(stemmer.stem(word))
                #keydata=key_idx.get(stemmer.stem(word,0,len(word)-1).lower(), None)
                if keydata: v[keydata[0]] = 1
        return v

f1 = open('f1.txt', 'r')
f2 = open('f2.txt','r')
s1, s2 = f1.read(), f2.read()
s1, s2 = s1.lower(), s2.lower()

v1=doc_vec(s1)
v2=doc_vec(s2)
print(v1)
print(v2)
print ("Similarity: %s" % float(dot(v1,v2) / (norm(v1) * norm(v2))))