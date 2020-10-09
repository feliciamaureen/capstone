import pandas as pd
import math
from preprocess import *

get60sLyrics()
get70sLyrics()
get80sLyrics()
get90sLyrics()
get00sLyrics()
get10sLyrics()

#get unique words
uniqueWords = set(wordsEurovision).union(set(words60s), set(words70s), set(words80s), set(words90s), set(words00s), set(words10s))

#create a dictionary of words and their occurence for each document
def wordCount(data):
    dictName = dict.fromkeys(uniqueWords, 0)
    for word in data:
        dictName[word] += 1
    return dictName

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

#returns dictionary of TF values
#basic IDF with log
def computeIDFBasic(documents):
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict 


def computeIDFPlusOne(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = 1 + math.log(N / float(val))
    return idfDict

def computeTFIDF(tfData, idfs):
    tfidf = {}
    for word, val in tfData.items():
        tfidf[word] = val * idfs[word]
    return tfidf

#word count
wcEV = wordCount(wordsEurovision)
wc60s = wordCount(words60s)
wc70s = wordCount(words70s)
wc80s = wordCount(words80s)
wc90s = wordCount(words90s)
wc00s = wordCount(words00s)
wc10s = wordCount(words10s)

#TF values 
tfEV = computeTF(wcEV, wordsEurovision)
tf60s = computeTF(wc60s, words60s)
tf70s = computeTF(wc60s, words70s)
tf80s = computeTF(wc60s, words80s)
tf90s = computeTF(wc60s, words90s)
tf10s = computeTF(wc60s, words10s)
tf00s = computeTF(wc60s, words00s)

#IDF values (basic idf, log)
allIDFBasic = computeIDFBasic([wcEV, wc60s, wc70s, wc80s, wc90s, wc00s, wc10s])
#IDF with plus one (basic idf, 1 + log)
allIDFPlusOne = computeIDFPlusOne([wcEV, wc60s, wc70s, wc80s, wc90s, wc00s, wc10s])

#basic ttfidf
tfidfBEV = computeTFIDF(tfEV, allIDFBasic)
tfidfB60s = computeTFIDF(tf60s, allIDFBasic)
tfidfB70s = computeTFIDF(tf70s, allIDFBasic)
tfidfB80s = computeTFIDF(tf80s, allIDFBasic)
tfidfB90s = computeTFIDF(tf90s, allIDFBasic)
tfidfB00s = computeTFIDF(tf00s, allIDFBasic)
tfidfB10s = computeTFIDF(tf10s, allIDFBasic)
dfBasic = pd.DataFrame([tfidfBEV, tfidfB60s, tfidfB70s, tfidfB80s, tfidfB90s, tfidfB00s, tfidfB10s])

#tfidf with idf plus one
tfidfPEV = computeTFIDF(tfEV, allIDFPlusOne)
tfidfP60s = computeTFIDF(tf60s, allIDFPlusOne)
tfidfP70s = computeTFIDF(tf70s, allIDFPlusOne)
tfidfP80s = computeTFIDF(tf80s, allIDFPlusOne)
tfidfP90s = computeTFIDF(tf90s, allIDFPlusOne)
tfidfP00s = computeTFIDF(tf00s, allIDFPlusOne)
tfidfP10s = computeTFIDF(tf10s, allIDFPlusOne)
dfPlusOne = pd.DataFrame([tfidfPEV, tfidfP60s, tfidfP70s, tfidfP80s, tfidfP90s, tfidfP00s, tfidfP10s])