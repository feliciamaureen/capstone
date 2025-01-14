"""
Word Processing

This script is used to calculate the TF-IDF and frequency values for the tokenized words

This script requires that 'pandas' and 'math' be installed within the Python environment you are running this script in.
and the class preprocess.py to get the tokenized words

This file can also be imported as a module and contains the following
functions: 
- wordCount: count the number of times a word occurs 
- computeTF: calculates term frequency
- computeIDFBasic: calculates inverse document frequency with the basic formula(math.log(dcTotal / float(val)))
- computeIDFPlusOne: calculates inverse document frequency with the modified formula (1 + math.log(dcTotal / float(val)))
- computeTFIDF: computes TF-IDF values
- getWordsFreqDF: gets dataframe of word frequencies
- getTop15Words: gets the top 15 words by index
- exportWordsExcel: exports all results to excel
"""

import pandas as pd
import math

from preprocess import *

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
top1560sB = dfBasic.nlargest(15, '60s')
top1570sB = dfBasic.nlargest(15, '70s')
top1580sB = dfBasic.nlargest(15, '80s')
top1590sB = dfBasic.nlargest(15, '90s')
top1500sB = dfBasic.nlargest(15, '00s')
top1510sB = dfBasic.nlargest(15, '10s')

#tfidf with idf plus one
tfidfPEV = computeTFIDF(tfEV, allIDFPlusOne)
tfidfP60s = computeTFIDF(tf60s, allIDFPlusOne)
tfidfP70s = computeTFIDF(tf70s, allIDFPlusOne)
tfidfP80s = computeTFIDF(tf80s, allIDFPlusOne)
tfidfP90s = computeTFIDF(tf90s, allIDFPlusOne)
tfidfP00s = computeTFIDF(tf00s, allIDFPlusOne)
tfidfP10s = computeTFIDF(tf10s, allIDFPlusOne)
tfidfPDecades = computeTFIDF(tfDecades, allIDFPlusOne)

#summarise results in dataframe
plusOneData = {'EV': tfidfPEV, '60s': tfidfP60s, '70s': tfidfP70s, '80s': tfidfP80s, '90s': tfidfP90s, '00s': tfidfP00s, '10s': tfidfP10s, 'decades': tfidfPDecades}
dfPlusOne = pd.DataFrame(data=plusOneData)

#top 15 values sorted by Eurovision and Decades
top15EVP = dfPlusOne.nlargest(15, 'EV')
top15DecadesP = dfPlusOne.nlargest(15, 'decades')
top1560sP = dfPlusOne.nlargest(15, '60s')
top1570sP = dfPlusOne.nlargest(15, '70s')
top1580sP = dfPlusOne.nlargest(15, '80s')
top1590sP = dfPlusOne.nlargest(15, '90s')
top1500sP = dfPlusOne.nlargest(15, '00s')
top1510sP = dfPlusOne.nlargest(15, '10s')

#for results summary
def getWordsFreqDF():
    return wordCount

def getTop15Words(index):
    top15Words = dfWordCount.nlargest(15, index)
    return top15Words

#top 15 words in each category based on frequency
dFreq = {'EV': getTop15Words('EV').index.values.tolist(), 
         '60s': getTop15Words('60s').index.values.tolist(), 
         '70s': getTop15Words('70s').index.values.tolist(), 
         '80s': getTop15Words('80s').index.values.tolist(), 
         '90s': getTop15Words('90s').index.values.tolist(),
         '00s': getTop15Words('00s').index.values.tolist(), 
         '10s': getTop15Words('10s').index.values.tolist(), 
         'decades': getTop15Words('decades').index.values.tolist()}
top15WordsResults = pd.DataFrame(data=dFreq)

#top 15 words in each category based on TF-IDF Basic
dTFIDFb = {'EV': top15EVB.index.values.tolist(), 
         '60s': top1560sB.index.values.tolist(), 
         '70s': top1570sB.index.values.tolist(), 
         '80s': top1580sB.index.values.tolist(), 
         '90s': top1590sB.index.values.tolist(),
         '00s': top1500sB.index.values.tolist(), 
         '10s': top1510sB.index.values.tolist(), 
         'decades': top15DecadesB.index.values.tolist()}
top15TFIDFBResults = pd.DataFrame(data=dTFIDFb)

#top 15 words in each category based on TF-IDF Plus One
dTFIDFp = {'EV': top15EVP.index.values.tolist(), 
         '60s': top1560sP.index.values.tolist(), 
         '70s': top1570sP.index.values.tolist(), 
         '80s': top1580sP.index.values.tolist(), 
         '90s': top1590sP.index.values.tolist(),
         '00s': top1500sP.index.values.tolist(), 
         '10s': top1510sP.index.values.tolist(), 
         'decades': top15DecadesP.index.values.tolist()}
top15TFIDFPResults = pd.DataFrame(data=dTFIDFp)

#export all results to excel
def exportWordsExcel():
    with pd.ExcelWriter('wordsTFIDF.xlsx') as writer:  
        top15WordsResults.to_excel(writer, sheet_name='Word Frequency')
        top15TFIDFBResults.to_excel(writer, sheet_name='TF-IDF Basic')
        top15TFIDFPResults.to_excel(writer, sheet_name='TF-IDF Plus One')
        