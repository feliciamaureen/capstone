import pandas as pd
import numpy as np
import nltk
import string

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

eurovisionLyrics = eurovision.read()
lyrics60s = c60s.read()
lyrics70s = c70s.read()
lyrics80s = c80s.read()
lyrics90s = c90s.read()
lyrics00s = c00s.read()
lyrics10s = c10s.read()

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

def cleanText(data):
    data = convLower(data)
    data = removePunctuation(data)
    return data

#clean lyrics
clean60s = cleanText(lyrics60s)
clean70s = cleanText(lyrics70s)
clean80s = cleanText(lyrics80s)
clean90s = cleanText(lyrics90s)
clean00s = cleanText(lyrics00s)
clean10s = cleanText(lyrics10s)

#tokenize as words
wordsEurovision = word_tokenize(eurovisionLyrics)
words60s = word_tokenize(clean60s)
words70s = word_tokenize(clean70s)
words80s = word_tokenize(clean80s)
words90s = word_tokenize(clean90s)
words00s = word_tokenize(clean00s)
words10s = word_tokenize(clean10s)

#tokenize to sentences - not perfect
senEurovision = sent_tokenize(eurovisionLyrics)
sen60s = sent_tokenize(clean60s)
sen70s = sent_tokenize(clean70s)
sen80s = sent_tokenize(clean80s)
sen90s = sent_tokenize(clean90s)
sen00s = sent_tokenize(clean00s)
sen10s = sent_tokenize(clean10s)

#for use in other classes
#lyrics
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

#words
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

#sentences
def get60sSen():
    return sen60s
def get70sSen():
    return sen70s
def get80sSen():
    return sen80s
def get90sSen():
    return sen90s
def get00sSen():
    return words00s
def get10sSen():
    return sen10s