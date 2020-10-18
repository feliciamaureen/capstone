"""
Bigram Processing

This script is used to make bigrams from the tokenized text and used to apply TF-IDF to the bigrams 
as well as get the top 15 bigrams in the documents

This script requires that 'pandas' and 'nltk' be installed within the Python environment you are running this script in.
and the classess words.py to get the tokenized words and preprocess.py to call the TF-IDF functions

This file can also be imported as a module and contains the following
functions: 
- bigramCount: count how many times a bigram occurs in the text
- getBGFreqDF: gets the dataframe containing bigram frequency
- getTop15Bigrams: gets the top 15 bigrams by an index
- exportBigramsExcel: export all the results to excel
- exportBigramsFreqExcel: exports all the the top 15 bigram frequency results to excel

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

#bigrams for each lyrics set
bgEV = list(nltk.bigrams(wordsEurovision))
bg60s = list(nltk.bigrams(words60s))
bg70s = list(nltk.bigrams(words70s))
bg80s = list(nltk.bigrams(words80s))
bg90s = list(nltk.bigrams(words90s))
bg00s = list(nltk.bigrams(words00s))
bg10s = list(nltk.bigrams(words10s))
bgDecades = list(nltk.bigrams(wordsDecades))

#get unique bigrams
uniqueBigrams = set(bgEV).union(set(bg60s), set(bg70s), set(bg80s), set(bg90s), set(bg00s), set(bg10s), set(bgDecades))

#bigram count
def bigramCount(data):
    dictName = dict.fromkeys(uniqueBigrams, 0)
    for i in data:
        dictName[i] += 1
    return dictName

bgcEV = bigramCount(bgEV)
bgc60s = bigramCount(bg60s)
bgc70s = bigramCount(bg70s)
bgc80s = bigramCount(bg80s)
bgc90s = bigramCount(bg90s)
bgc00s = bigramCount(bg00s)
bgc10s = bigramCount(bg10s)
bgcDecades = bigramCount(bgDecades)

#df of bigram frequency
biGramCount = {'EV': bgcEV, '60s': bgc60s, '70s': bgc70s, '80s': bgc80s, '90s': bgc90s, '00s': bgc00s, '10s': bgc10s, 'decades': bgcDecades}
dfBigramCount = pd.DataFrame(data=biGramCount)


#TF values for bigrams
tfbgEV = computeTF(bgcEV, bgEV)
tfbg60s = computeTF(bgc60s, bg60s)
tfbg70s = computeTF(bgc70s, bg70s)
tfbg80s = computeTF(bgc80s, bg80s)
tfbg90s = computeTF(bgc90s, bg90s)
tfbg10s = computeTF(bgc00s, bg00s)
tfbg00s = computeTF(bgc10s, bg10s)
tfbgDecades = computeTF(bgcDecades, bgDecades)

#basic IDF value for bigrams
bgIDF = computeIDFBasic([bgcEV, bgc60s, bgc70s, bgc80s, bgc90s, bgc00s, bgc10s, bgcDecades])
#IDF with plus one (basic idf, 1 + log)
bgIDFPlusOne = computeIDFPlusOne([bgcEV, bgc60s, bgc70s, bgc80s, bgc90s, bgc00s, bgc10s, bgcDecades])

#basic tfidf values
tfidfBigramEV = computeTFIDF(tfbgEV, bgIDF)
tfidfBigram60s = computeTFIDF(tfbg60s, bgIDF)
tfidfBigram70s = computeTFIDF(tfbg70s, bgIDF)
tfidfBigram80s = computeTFIDF(tfbg80s, bgIDF)
tfidfBigram90s = computeTFIDF(tfbg90s, bgIDF)
tfidfBigram00s = computeTFIDF(tfbg00s, bgIDF)
tfidfBigram10s = computeTFIDF(tfbg10s, bgIDF)
tfidfBigramDecades = computeTFIDF(tfbgDecades, bgIDF)

#summarise results in dataframe
biGramDataB = {'EV': tfidfBigramEV, '60s': tfidfBigram60s, '70s': tfidfBigram70s, '80s': tfidfBigram80s, '90s': tfidfBigram90s, '00s': tfidfBigram00s, '10s': tfidfBigram10s, 'decades': tfidfBigramDecades}
dfBigramB = pd.DataFrame(data=biGramDataB)

#top 15 values sorted by columns
top15bgEVB = dfBigramB.nlargest(15, 'EV')
top15bgDecadesB = dfBigramB.nlargest(15, 'decades')
top15bg60sB = dfBigramB.nlargest(15, '60s')
top15bg70sB = dfBigramB.nlargest(15, '70s')
top15bg80sB = dfBigramB.nlargest(15, '80s')
top15bg90sB = dfBigramB.nlargest(15, '90s')
top15bg00sB = dfBigramB.nlargest(15, '00s')
top15bg10sB = dfBigramB.nlargest(15, '10s')

#tfidf with idf plus one
tfidfBigramEVP = computeTFIDF(tfbgEV, bgIDFPlusOne)
tfidfBigram60sP = computeTFIDF(tfbg60s, bgIDFPlusOne)
tfidfBigram70sP = computeTFIDF(tfbg70s, bgIDFPlusOne)
tfidfBigram80sP = computeTFIDF(tfbg80s, bgIDFPlusOne)
tfidfBigram90sP = computeTFIDF(tfbg90s, bgIDFPlusOne)
tfidfBigram00sP = computeTFIDF(tfbg00s, bgIDFPlusOne)
tfidfBigram10sP = computeTFIDF(tfbg10s, bgIDFPlusOne)
tfidfBigramDecadesP = computeTFIDF(tfbgDecades, bgIDFPlusOne)

#summarise plus one results in dataframe
bigramDataP = {'EV': tfidfBigramEVP, '60s': tfidfBigram60sP, '70s': tfidfBigram70sP, '80s': tfidfBigram80sP, '90s': tfidfBigram90sP, '00s': tfidfBigram00sP, '10s': tfidfBigram10sP, 'decades': tfidfBigramDecadesP}
dfBigramP = pd.DataFrame(data=bigramDataP)

#top 15 values sorted by columns
top15bgEVP = dfBigramP.nlargest(15, 'EV')
top15bgDecadesP = dfBigramP.nlargest(15, 'decades')
top15bg60sP = dfBigramP.nlargest(15, '60s')
top15bg70sP = dfBigramP.nlargest(15, '70s')
top15bg80sP = dfBigramP.nlargest(15, '80s')
top15bg90sP = dfBigramP.nlargest(15, '90s')
top15bg00sP = dfBigramP.nlargest(15, '00s')
top15bg10sP = dfBigramP.nlargest(15, '10s')


#for results summary
def getBGFreqDF():
    return dfBigramCount

def getTop15Bigrams(index):
    top15Bigrams = dfBigramCount.nlargest(15, index)
    return top15Bigrams

def exportBigramsExcel():
    with pd.ExcelWriter('bigramsTFIDF.xlsx') as writer:  
        top15bgEVB.to_excel(writer, sheet_name='bigrams eurovision basic')
        top15bgDecadesB.to_excel(writer, sheet_name='bigrams decades basic ')
        top15bg60sB.to_excel(writer, sheet_name='bigrams basic 60s')
        top15bg70sB.to_excel(writer, sheet_name='bigrams basic 70s')
        top15bg80sB.to_excel(writer, sheet_name='bigrams basic 80s')
        top15bg90sB.to_excel(writer, sheet_name='bigrams basic 90s')
        top15bg00sB.to_excel(writer, sheet_name='bigrams basic 00s')
        top15bg10sB.to_excel(writer, sheet_name='bigrams basic 10s')

        top15bgEVP.to_excel(writer, sheet_name='bigrams eurovision plus one')
        top15bgDecadesP.to_excel(writer, sheet_name='bigrams decades plus one ')
        top15bg60sP.to_excel(writer, sheet_name='bigrams plus one 60s')
        top15bg70sP.to_excel(writer, sheet_name='bigrams plus one 70s')
        top15bg80sP.to_excel(writer, sheet_name='bigrams plus one 80s')
        top15bg90sP.to_excel(writer, sheet_name='bigrams plus one 90s')
        top15bg00sP.to_excel(writer, sheet_name='bigrams plus one 00s')
        top15bg10sP.to_excel(writer, sheet_name='bigrams plus one 10s')

def exportBigramsFreqExcel():
    with pd.ExcelWriter('bgFrequency.xlsx') as writer:  
        getTop15Bigrams('EV').to_excel(writer, sheet_name='eurovision')
        getTop15Bigrams('decades').to_excel(writer, sheet_name='decades')
        getTop15Bigrams('60s').to_excel(writer, sheet_name='60s')
        getTop15Bigrams('70s').to_excel(writer, sheet_name='70s')
        getTop15Bigrams('80s').to_excel(writer, sheet_name='80s')
        getTop15Bigrams('90s').to_excel(writer, sheet_name='90s')
        getTop15Bigrams('00s').to_excel(writer, sheet_name='00s')
        getTop15Bigrams('10s').to_excel(writer, sheet_name='10s')

       