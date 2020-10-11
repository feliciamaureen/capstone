import nltk
import pandas as pd
from words import wordCount, computeTF, computeIDFBasic, computeIDFPlusOne, computeTFIDF
from preprocess import *

#import lyrics tokenized as words
get60sWords()
get70sWords()
get80sWords()
get90sWords()
get00sWords()
get10sWords()
getDecadesLyrics()

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

def getBGFreqDF():
    return dfBigramCount

def getTop15Bigrams(index):
    top15Bigrams = dfBigramCount.nlargest(15, index)
    return top15Bigrams.index.values

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

#tfidf values
tfidfBigramEV = computeTFIDF(tfbgEV, bgIDF)
tfidfBigram60s = computeTFIDF(tfbg60s, bgIDF)
tfidfBigram70s = computeTFIDF(tfbg70s, bgIDF)
tfidfBigram80s = computeTFIDF(tfbg80s, bgIDF)
tfidfBigram90s = computeTFIDF(tfbg90s, bgIDF)
tfidfBigram00s = computeTFIDF(tfbg00s, bgIDF)
tfidfBigram10s = computeTFIDF(tfbg10s, bgIDF)
tfidfBigramDecades = computeTFIDF(tfbgDecades, bgIDF)

#summarise results in dataframe
biGramData = {'EV': tfidfBigramEV, '60s': tfidfBigram60s, '70s': tfidfBigram70s, '80s': tfidfBigram80s, '90s': tfidfBigram90s, '00s': tfidfBigram00s, '10s': tfidfBigram10s, 'decades': tfidfBigramDecades}
dfBigram = pd.DataFrame(data=biGramData)

#top 15 values sorted by Eurovision and Decades
top15bgEV = dfBigram.nlargest(15, 'EV')
top15bgDecades = dfBigram.nlargest(15, 'decades')

