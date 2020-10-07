import pandas as pd
from preprocess import *

get60sLyrics()
get70sLyrics()
get80sLyrics()
get90sLyrics()
get00sLyrics()
get10sLyrics()

#create a dictionary of words and their occurence for each document
def wordCount(data):
    dictName = dict.fromkeys(data, 0)
    for word in dictName:
        dictName[word] += 1
    return dictName

def computeTF(wordDict, data):
    tfDict = {}
    wordCount = len(data)
    for word, count in wordDict.items():
        tfDict[word] = count / float(wordCount)
    return tfDict

#returns dictionary of TF values
#basic IDF with log
def computeIDFBasic(documents):
    import math
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
decadeIDFBasic = computeIDFBasic([tf60s, tf70s, tf80s, tf90s, tf00s, tf10s])
#allIDFBasic = computeIDFBasic([tfEV, tf60s, tf70s, tf80s, tf90s, tf00s, tf10s]) --> broken, key error "makeup"

#IDF with plus one (basic idf, 1 + log)
decadeIDFPlusOne = computeIDFPlusOne([tf60s, tf70s, tf80s, tf90s, tf00s, tf10s])
#allIDFPlusOne = computeIDFPlusOne([tfEV, tf60s, tf70s, tf80s, tf90s, tf00s, tf10s])

#basic ttfidf
tfidfB60s = computeTFIDF(tf60s, decadeIDFBasic)
tfidfB70s = computeTFIDF(tf70s, decadeIDFBasic)
tfidfB80s = computeTFIDF(tf80s, decadeIDFBasic)
tfidfB90s = computeTFIDF(tf90s, decadeIDFBasic)
tfidfB00s = computeTFIDF(tf00s, decadeIDFBasic)
tfidfB10s = computeTFIDF(tf10s, decadeIDFBasic)
dfBasic = pd.DataFrame([tfidfB60s, tfidfB70s, tfidfB80s, tfidfB90s, tfidfB00s, tfidfB10s])

#tfidf with idf plus one
tfidfP60s = computeTFIDF(tf60s, decadeIDFPlusOne)
tfidfP70s = computeTFIDF(tf70s, decadeIDFPlusOne)
tfidfP80s = computeTFIDF(tf80s, decadeIDFPlusOne)
tfidfP90s = computeTFIDF(tf90s, decadeIDFPlusOne)
tfidfP00s = computeTFIDF(tf00s, decadeIDFPlusOne)
tfidfP10s = computeTFIDF(tf10s, decadeIDFPlusOne)
dfPlusOne = pd.DataFrame([tfidfP60s, tfidfP70s, tfidfP80s, tfidfP90s, tfidfP00s, tfidfP10s])