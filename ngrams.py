import nltk
from preprocess import *

#import lyrics tokenized as words
get60sWords()
get70sWords()
get80sWords()
get90sWords()
get00sWords()
get10sWords()

#bigrams 2010s
bigrams10s = nltk.bigrams(words10s)
filteredBigrams10s = [ (w1, w2) for w1, w2 in bigrams10s if len(w1) >=5 and len(w2) >= 5 ]
bifreq10s = nltk.FreqDist(filteredBigrams10s)
print(bifreq10s.most_common(3))

#bigrams 2000s
bigrams00s = nltk.bigrams(words00s)
filteredBigrams00s = [ (w1, w2) for w1, w2 in bigrams00s if len(w1) >=5 and len(w2) >= 5 ]
bifreq00s = nltk.FreqDist(filteredBigrams00s)

#bigrams 1990s
bigrams90s = nltk.bigrams(words90s)
filteredBigrams90s = [ (w1, w2) for w1, w2 in bigrams90s if len(w1) >=5 and len(w2) >= 5 ]
bifreq90s = nltk.FreqDist(filteredBigrams90s)

#bigrams 1980s
bigrams80s = nltk.bigrams(words80s)
filteredBigrams80s = [ (w1, w2) for w1, w2 in bigrams80s if len(w1) >=5 and len(w2) >= 5 ]
bifreq80s = nltk.FreqDist(filteredBigrams80s)

#bigrams 1970s
bigrams70s = nltk.bigrams(words70s)
filteredBigrams70s = [ (w1, w2) for w1, w2 in bigrams70s if len(w1) >=5 and len(w2) >= 5 ]
bifreq70s = nltk.FreqDist(filteredBigrams70s)

#bigrams 1960s
bigrams60s = nltk.bigrams(words60s)
filteredBigrams60s = [ (w1, w2) for w1, w2 in bigrams60s if len(w1) >=5 and len(w2) >= 5 ]
bifreq60s = nltk.FreqDist(filteredBigrams60s)

#bigrams Eurovision
bigramsEurovision = nltk.bigrams(wordsEurovision)
filteredBigramsEV = [ (w1, w2) for w1, w2 in bigramsEurovision if len(w1) >=5 and len(w2) >= 5 ]
bifreqEV = nltk.FreqDist(filteredBigramsEV)

#print top 3 bigrams
print(bifreq00s.most_common(3))
print(bifreq10s.most_common(3))
print(bifreq90s.most_common(3))
print(bifreq80s.most_common(3))
print(bifreq70s.most_common(3))
print(bifreq60s.most_common(3))
print(bifreqEV.most_common(3))
