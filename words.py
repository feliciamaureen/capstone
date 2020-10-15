import pandas as pd
import math

from preprocess import *
from tfidf import *

#import lyrics tokenized as words
wordsEurovision = getEVWords()
words60s = get60sWords()
words70s = get70sWords()
words80s = get80sWords()
words90s = get90sWords()
words00s = get00sWords()
words10s = get10sWords()
wordsDecades = getDecadesWords()
dcTotal = getTotalCount()

#create a dictionary of words and their occurence for each document
def wordCount(data):
    dictName = dict.fromkeys(uniqueWords, 0)
    for word in data:
        dictName[word] += 1
    return dictName

#compute TF value for each set of lyrics
#returns dictionary of TF values
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

#basic IDF formula
#N = the number of documents from docCount
def computeIDFBasic(documents):
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(dcTotal / float(val))
    return idfDict 

#modified IDF with +1
#N = the number of documents from docCount
def computeIDFPlusOne(documents):
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = 1 + math.log(dcTotal / float(val))
    return idfDict

#compute TF-IDF value
def computeTFIDF(tfData, idfs):
    tfidf = {}
    for word, val in tfData.items():
        tfidf[word] = val * idfs[word]
    return tfidf

#get unique words
uniqueWords = set(wordsEurovision).union(set(words60s), set(words70s), set(words80s), set(words90s), set(words00s), set(words10s), set(wordsDecades))

#word count
wcEV = wordCount(wordsEurovision)
wcDecades = wordCount(wordsDecades)
wc60s = wordCount(words60s)
wc70s = wordCount(words70s)
wc80s = wordCount(words80s)
wc90s = wordCount(words90s)
wc00s = wordCount(words00s)
wc10s = wordCount(words10s)

#df of word frequency
wordCount = {'EV': wcEV, '60s': wc60s, '70s': wc70s, '80s': wc80s, '90s': wc90s, '00s': wc00s, '10s': wc10s, 'decades': wcDecades}
dfWordCount = pd.DataFrame(data=wordCount)

#TF values 
tfEV = computeTF(wcEV, wordsEurovision)
tf60s = computeTF(wc60s, words60s)
tf70s = computeTF(wc70s, words70s)
tf80s = computeTF(wc80s, words80s)
tf90s = computeTF(wc90s, words90s)
tf00s = computeTF(wc00s, words00s)
tf10s = computeTF(wc10s, words10s)
tfDecades = computeTF(wcDecades, wordsDecades)

#IDF values (basic idf, log)
allIDFBasic = computeIDFBasic([wcEV, wc60s, wc70s, wc80s, wc90s, wc00s, wc10s, wcDecades])
#IDF with plus one (basic idf, 1 + log)
allIDFPlusOne = computeIDFPlusOne([wcEV, wc60s, wc70s, wc80s, wc90s, wc00s, wc10s, wcDecades])

#basic ttfidf
tfidfBEV = computeTFIDF(tfEV, allIDFBasic)
tfidfB60s = computeTFIDF(tf60s, allIDFBasic)
tfidfB70s = computeTFIDF(tf70s, allIDFBasic)
tfidfB80s = computeTFIDF(tf80s, allIDFBasic)
tfidfB90s = computeTFIDF(tf90s, allIDFBasic)
tfidfB00s = computeTFIDF(tf00s, allIDFBasic)
tfidfB10s = computeTFIDF(tf10s, allIDFBasic)
tfidfBDecades = computeTFIDF(tfDecades, allIDFBasic)

#summarise results in dataframe
basicData = {'EV': tfidfBEV, '60s': tfidfB60s, '70s': tfidfB70s, '80s': tfidfB80s, '90s': tfidfB90s, '00s': tfidfB00s, '10s': tfidfB10s, 'decades': tfidfBDecades}
dfBasic = pd.DataFrame(data=basicData)

#top 15 values sorted by Eurovision and Decades
top15EVB = dfBasic.nlargest(15, 'EV')
top15DecadesB = dfBasic.nlargest(15, 'decades')

#tfidf with idf plus one
tfidfPEV = computeTFIDF(tfEV, allIDFPlusOne)
tfidfP60s = computeTFIDF(tf60s, allIDFPlusOne)
tfidfP70s = computeTFIDF(tf70s, allIDFPlusOne)
tfidfP80s = computeTFIDF(tf80s, allIDFPlusOne)
tfidfP90s = computeTFIDF(tf90s, allIDFPlusOne)
tfidfP00s = computeTFIDF(tf00s, allIDFPlusOne)
tfidfP10s = computeTFIDF(tf10s, allIDFPlusOne)
tfidfPDecades = computeTFIDF(tfDecades, allIDFPlusOne)

plusOneData = {'EV': tfidfPEV, '60s': tfidfP60s, '70s': tfidfP70s, '80s': tfidfP80s, '90s': tfidfP90s, '00s': tfidfP00s, '10s': tfidfP10s, 'decades': tfidfPDecades}
dfPlusOne = pd.DataFrame(data=plusOneData)

#top 15 values sorted by Eurovision and Decades
top15EVP = dfPlusOne.nlargest(15, 'EV')
top15DecadesP = dfPlusOne.nlargest(15, 'decades')

#for results summary
def getWordsFreqDF():
    return wordCount

def getTop15Words(index):
    top15Words = dfWordCount.nlargest(15, index)
    return top15Words

def exportWordsExcel():
    with pd.ExcelWriter('wordsTFIDF.xlsx') as writer:  
        top15Bigrams = getTop15Words
        top15DecadesB.to_excel(writer, sheet_name='decades basic')
        top15DecadesP.to_excel(writer, sheet_name='decades plus one')
        top15EVB.to_excel(writer, sheet_name='eurovision basic')
        top15EVP.to_excel(writer, sheet_name='eurovision plus one')
        top15Bigrams.to_excel(writer, sheet_name='top 15 words')