"""
Trigram Processing

This script is used to make trigrams from the tokenized text and used to apply TF-IDF to the trigrams 
as well as get the top 15 trigrams in the documents

This script requires that 'pandas' and 'nltk' be installed within the Python environment you are running this script in.
and the classess words.py to get the tokenized words and preprocess.py to call the TF-IDF functions

This file can also be imported as a module and contains the following
functions: 
- trigramCount: count how many times a trigram occurs in the text
- getTGFreqDF: gets the dataframe containing trigram frequency
- getTop15Bigrams: gets the top 15 trigrams by an index
- exportTrigramsExcel: export all the TF-IDF results  results to excel
- exportTrigramsFreqExcel: exports all the the top 15  trigram frequency results to excel
"""

import nltk
import pandas as pd
from words import wordCount, computeTF, computeIDFBasic, computeIDFPlusOne, computeTFIDF
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

#trigrams for each lyrics set
tgEV = list(nltk.trigrams(wordsEurovision))
tg60s = list(nltk.trigrams(words60s))
tg70s = list(nltk.trigrams(words70s))
tg80s = list(nltk.trigrams(words80s))
tg90s = list(nltk.trigrams(words90s))
tg00s = list(nltk.trigrams(words00s))
tg10s = list(nltk.trigrams(words10s))
tgDecades = list(nltk.trigrams(wordsDecades))

#get unique trigrams
uniqueTrigrams = set(tgEV).union(set(tg60s), set(tg70s), set(tg80s), set(tg90s), set(tg00s), set(tg10s), set(tgDecades))

#trigram count
def trigramCount(data):
    dictName = dict.fromkeys(uniqueTrigrams, 0)
    for i in data:
        dictName[i] += 1
    return dictName

tgcEV = trigramCount(tgEV)
tgc60s = trigramCount(tg60s)
tgc70s = trigramCount(tg70s)
tgc80s = trigramCount(tg80s)
tgc90s = trigramCount(tg90s)
tgc00s = trigramCount(tg00s)
tgc10s = trigramCount(tg10s)
tgcDecades = trigramCount(tgDecades)

#df of trigram frequency
triGramCount = {'EV': tgcEV, '60s': tgc60s, '70s': tgc70s, '80s': tgc80s, '90s': tgc90s, '00s': tgc00s, '10s': tgc10s, 'decades': tgcDecades}
dfTrigramCount = pd.DataFrame(data=triGramCount)

#TF values for trigrams
tftgEV = computeTF(tgcEV, tgEV)
tftg60s = computeTF(tgc60s, tg60s)
tftg70s = computeTF(tgc70s, tg70s)
tftg80s = computeTF(tgc80s, tg80s)
tftg90s = computeTF(tgc90s, tg90s)
tftg10s = computeTF(tgc00s, tg00s)
tftg00s = computeTF(tgc10s, tg10s)
tftgDecades = computeTF(tgcDecades, tgDecades)

#basic IDF value for trigrams
tgIDF = computeIDFBasic([tgcEV, tgc60s, tgc70s, tgc80s, tgc90s, tgc00s, tgc10s, tgcDecades])
#IDF with plus one (basic idf, 1 + log)
tgIDFPlusOne = computeIDFPlusOne([tgcEV, tgc60s, tgc70s, tgc80s, tgc90s, tgc00s, tgc10s, tgcDecades])

#basic fidf values
tfidfTrigramEVB = computeTFIDF(tftgEV, tgIDF)
tfidfTrigram60sB = computeTFIDF(tftg60s, tgIDF)
tfidfTrigram70sB = computeTFIDF(tftg70s, tgIDF)
tfidfTrigram80sB = computeTFIDF(tftg80s, tgIDF)
tfidfTrigram90sB = computeTFIDF(tftg90s, tgIDF)
tfidfTrigram00sB = computeTFIDF(tftg00s, tgIDF)
tfidfTrigram10sB = computeTFIDF(tftg10s, tgIDF)
tfidfTrigramDecadesB = computeTFIDF(tftgDecades, tgIDF)

#summarise baisc results in dataframe
triGramDataB = {'EV': tfidfTrigramEVB, '60s': tfidfTrigram60sB, '70s': tfidfTrigram70sB, '80s': tfidfTrigram80sB, '90s': tfidfTrigram90sB, '00s': tfidfTrigram00sB, '10s': tfidfTrigram10sB, 'decades': tfidfTrigramDecadesB}
dfTrigramB = pd.DataFrame(data=triGramDataB)

#top 15 values sorted by columns
top15tgEVB = dfTrigramB.nlargest(15, 'EV')
top15tgDecadesB = dfTrigramB.nlargest(15, 'decades')
top15tg60sB = dfTrigramB.nlargest(15, '60s')
top15tg70sB = dfTrigramB.nlargest(15, '70s')
top15tg80sB = dfTrigramB.nlargest(15, '80s')
top15tg90sB = dfTrigramB.nlargest(15, '90s')
top15tg00sB = dfTrigramB.nlargest(15, '00s')
top15tg10sB = dfTrigramB.nlargest(15, '10s')

#tfidf with idf plus one
tfidfTrigramEVP = computeTFIDF(tftgEV, tgIDFPlusOne)
tfidfTrigram60sP = computeTFIDF(tftg60s, tgIDFPlusOne)
tfidfTrigram70sP = computeTFIDF(tftg70s, tgIDFPlusOne)
tfidfTrigram80sP = computeTFIDF(tftg80s, tgIDFPlusOne)
tfidfTrigram90sP = computeTFIDF(tftg90s, tgIDFPlusOne)
tfidfTrigram00sP = computeTFIDF(tftg00s, tgIDFPlusOne)
tfidfTrigram10sP = computeTFIDF(tftg10s, tgIDFPlusOne)
tfidfTrigramDecadesP = computeTFIDF(tftgDecades, tgIDFPlusOne)

#summarise plus one results in dataframe
triGramDataP = {'EV': tfidfTrigramEVP, '60s': tfidfTrigram60sP, '70s': tfidfTrigram70sP, '80s': tfidfTrigram80sP, '90s': tfidfTrigram90sP, '00s': tfidfTrigram00sB, '10s': tfidfTrigram10sP, 'decades': tfidfTrigramDecadesP}
dfTrigramP = pd.DataFrame(data=triGramDataP)

#top 15 values sorted by columns
top15tgEVP = dfTrigramP.nlargest(15, 'EV')
top15tgDecadesP = dfTrigramP.nlargest(15, 'decades')
top15tg60sP = dfTrigramP.nlargest(15, '60s')
top15tg70sP = dfTrigramP.nlargest(15, '70s')
top15tg80sP = dfTrigramP.nlargest(15, '80s')
top15tg90sP = dfTrigramP.nlargest(15, '90s')
top15tg00sP = dfTrigramP.nlargest(15, '00s')
top15tg10sP = dfTrigramP.nlargest(15, '10s')

#for results summary
def getTGFreqDF():
    return dfTrigramCount

def getTop15Trigrams(index):
    top15Trigrams = dfTrigramCount.nlargest(15, index)
    return top15Trigrams

def exportTrigramsExcel():
    with pd.ExcelWriter('trigramsTFIDF.xlsx') as writer:  
        top15tgEVB.to_excel(writer, sheet_name='trigrams eurovision basic')
        top15tgDecadesB.to_excel(writer, sheet_name='trigrams decades basic ')
        top15tg60sB.to_excel(writer, sheet_name='trigrams basic 60s')
        top15tg70sB.to_excel(writer, sheet_name='trigrams basic 70s')
        top15tg80sB.to_excel(writer, sheet_name='trigrams basic 80s')
        top15tg90sB.to_excel(writer, sheet_name='trigrams basic 90s')
        top15tg00sB.to_excel(writer, sheet_name='trigrams basic 00s')
        top15tg10sB.to_excel(writer, sheet_name='trigrams basic 10s')

        top15tgEVP.to_excel(writer, sheet_name='trigrams eurovision plus one')
        top15tgDecadesP.to_excel(writer, sheet_name='trigrams decades plus one ')
        top15tg60sP.to_excel(writer, sheet_name='trigrams plus one 60s')
        top15tg70sP.to_excel(writer, sheet_name='trigrams plus one 70s')
        top15tg80sP.to_excel(writer, sheet_name='trigrams plus one 80s')
        top15tg90sP.to_excel(writer, sheet_name='trigrams plus one 90s')
        top15tg00sP.to_excel(writer, sheet_name='trigrams plus one 00s')
        top15tg10sP.to_excel(writer, sheet_name='trigrams plus one 10s')

def exportTrigramsFreqExcel():
    with pd.ExcelWriter('tgFrequency.xlsx') as writer:  
        getTop15Trigrams('EV').to_excel(writer, sheet_name='eurovision')
        getTop15Trigrams('decades').to_excel(writer, sheet_name='decades')
        getTop15Trigrams('60s').to_excel(writer, sheet_name='60s')
        getTop15Trigrams('70s').to_excel(writer, sheet_name='70s')
        getTop15Trigrams('80s').to_excel(writer, sheet_name='80s')
        getTop15Trigrams('90s').to_excel(writer, sheet_name='90s')
        getTop15Trigrams('00s').to_excel(writer, sheet_name='00s')
        getTop15Trigrams('10s').to_excel(writer, sheet_name='10s')