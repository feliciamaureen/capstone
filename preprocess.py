import pandas as pd
import numpy as np
import nltk
import string
import re

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

#lyric files
eurovision = open("data/intersection.txt", "r")
c60s = open("data/1960s.txt", "r")
c70s = open("data/1970s.txt", "r")
c80s = open("data/1980s.txt", "r")
c90s = open("data/1990s.txt", "r")
c00s = open("data/2000s.txt", "r")
c10s = open("data/2010s.txt", "r")

#read lyric fules and store as variable
eurovisionLyrics = eurovision.read()
lyrics60s = c60s.read()
lyrics70s = c70s.read()
lyrics80s = c80s.read()
lyrics90s = c90s.read()
lyrics00s = c00s.read()
lyrics10s = c10s.read()

#close all text files
eurovision.close()
c60s.close()
c70s.close()
c80s.close()
c90s.close()
c00s.close()
c10s.close()

#make lowercase
def convLower(text):
    text = text.lower()
    return text

#remove punctuation
def removePunctuation(text):
    text = "".join([char for char in text if char not in string.punctuation])
    return text

#remove non-alphabet characters
def removeNonAlphabet(text):
    regex = re.sub(r'[^a-zA-Z]', '', text) 
    return text

#remove numbers
def removeNumbers(text):
    text = "".join(i for i in text if not i.isdigit())
    return text

#apply all cleaning functions to data
def cleanText(data):
    data = convLower(data)
    data = removePunctuation(data)
    data = removeNonAlphabet(data)
    data = removeNumbers(data)
    data = removePunctuation(data)
    return data

#count how many documents are in the text file, marked by '-----'
#dcEV = eurovisionLyrics.count('-----')
dc60s = lyrics60s.count('-----')
dc70s = lyrics70s.count('-----')
dc80s = lyrics80s.count('-----')
dc90s = lyrics90s.count('-----')
dc00s = lyrics00s.count('-----')
dc10s = lyrics10s.count('-----')
dcTotal = dc60s + dc70s + dc80s + dc90s + dc00s + dc10s #currently missing ev
#dcTotal = dcEV + dc60s + dc70s + dc80s + dc90s + dc00s + dc10s #currently missing ev

#clean lyrics
cleanEV = cleanText(eurovisionLyrics)
clean60s = cleanText(lyrics60s)
clean70s = cleanText(lyrics70s)
clean80s = cleanText(lyrics80s)
clean90s = cleanText(lyrics90s)
clean00s = cleanText(lyrics00s)
clean10s = cleanText(lyrics10s)
cleanDecades = clean60s + clean70s + clean80s + clean90s + clean00s + clean10s

#tokenize as words
wordsEurovision = word_tokenize(cleanEV)
words60s = word_tokenize(clean60s)
words70s = word_tokenize(clean70s)
words80s = word_tokenize(clean80s)
words90s = word_tokenize(clean90s)
words00s = word_tokenize(clean00s)
words10s = word_tokenize(clean10s)
wordsDecades = word_tokenize(cleanDecades)

#for use in other classes
#lyrics
def getEVLyrics():
    return cleanEV
def get60sLyrics():
    return clean60s
def get70sLyrics():
    return clean70s
def get80sLyrics():
    return clean90s
def get90sLyrics():
    return clean90s
def get00sLyrics():
    return clean00s
def get10sLyrics():
    return clean10s
def getDecadesLyrics():
    return cleanDecades

#words
def getEVWords():
    return wordsEurovision
def get60sWords():
    return words60s
def get70sWords():
    return words70s
def get80sWords():
    return words80s
def get90sWords():
    return words90s
def get00sWords():
    return words00s
def get10sWords():
    return words10s
def getDecadesWords():
    return wordsDecades

#document count
def getEVCount():
    return dcEV
def get60sCount():
    return dc60s
def get70sCount():
    return dc60s
def get80sCount():
    return dc60s
def get90sCount():
    return dc60s
def get00sCount():
    return dc60s
def get10sCount():
    return dc60s
def getTotalCount():
    return dcTotal

