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

#df of bigram frequency
triGramCount = {'EV': tgcEV, '60s': tgc60s, '70s': tgc70s, '80s': tgc80s, '90s': tgc90s, '00s': tgc00s, '10s': tgc10s, 'decades': tgcDecades}
dfTrigramCount = pd.DataFrame(data=triGramCount)

#TF values for bigrams
tftgEV = computeTF(tgcEV, tgEV)
tftg60s = computeTF(tgc60s, tg60s)
tftg70s = computeTF(tgc70s, tg70s)
tftg80s = computeTF(tgc80s, tg80s)
tftg90s = computeTF(tgc90s, tg90s)
tftg10s = computeTF(tgc00s, tg00s)
tftg00s = computeTF(tgc10s, tg10s)
tftgDecades = computeTF(tgcDecades, tgDecades)

#basic IDF value for bigrams
tgIDF = computeIDFBasic([tgcEV, tgc60s, tgc70s, tgc80s, tgc90s, tgc00s, tgc10s, tgcDecades])

#tfidf values
tfidfTrigramEV = computeTFIDF(tftgEV, tgIDF)
tfidfTrigram60s = computeTFIDF(tftg60s, tgIDF)
tfidfTrigram70s = computeTFIDF(tftg70s, tgIDF)
tfidfTrigram80s = computeTFIDF(tftg80s, tgIDF)
tfidfTrigram90s = computeTFIDF(tftg90s, tgIDF)
tfidfTrigram00s = computeTFIDF(tftg00s, tgIDF)
tfidfTrigram10s = computeTFIDF(tftg10s, tgIDF)
tfidfTrigramDecades = computeTFIDF(tftgDecades, tgIDF)

#summarise results in dataframe
triGramData = {'EV': tfidfTrigramEV, '60s': tfidfTrigram60s, '70s': tfidfTrigram70s, '80s': tfidfTrigram80s, '90s': tfidfTrigram90s, '00s': tfidfTrigram00s, '10s': tfidfTrigram10s, 'decades': tfidfTrigramDecades}
dfTrigram = pd.DataFrame(data=triGramData)

#top 15 values sorted by Eurovision and Decades
top15tgEV = dfTrigram.nlargest(15, 'EV')
top15tgDecades = dfTrigram.nlargest(15, 'decades')

#for results summary
def getTGFreqDF():
    return dfTrigramCount

def getTop15Trigrams(index):
    top15Trigrams = dfTrigramCount.nlargest(15, index)
    return top15Trigrams.index.values

def exportTrigramsExcel():
    top15Trigrams = getTop15Trigrams()
    with pd.ExcelWriter('bigramsTFIDF.xlsx') as writer:  
        top15tgEV.to_excel(writer, sheet_name='bigrams basic')
        top15tgDecades.to_excel(writer, sheet_name='bigrams plus one')
        top15Trigrams.to_excel(writer, sheet_name='top 15 trigrams')
