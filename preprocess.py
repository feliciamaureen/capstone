"""
Data Preprocessing

This script is used to clean and prepare the collected data before using it for analysis. 
It takes txt files containing the lyrics and a csv file of metadata of the Eurovision songs.

This script requires that 'pandas', 'numpy', 'nltk', 'string', and 're'  be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions: 
- convLower: converts all text to lower case
- removePunctuation: removes punctuation from text
- removeNumbers: removes numbers from text
- wordSplit: split a word into a list containing its characters
- removeConcat: removes apostrophes from contractions
- cleanText: calls all the methods above to apply all of them to the data
- findArtist: find artist in intersection.txt to count the number of songs

get functions for the list of tokenized words: to use in other classes that need the tokenized text
- getEVWords()
- get60sWords()
- get70sWords()
- get80sWords()
- get90sWords()
- get00sWords()
- get10sWords()
- getDecadesWords()

get functions for document count: to use in other classes that need the document count
- getEVCount()
- get60sCount()
- get70sCount()
- get80sCount()
- get90sCount()
- get00sCount()
- get10sCount()
- getTotalCount()
"""
import pandas as pd
import numpy as np
import nltk
import string
import re

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

#lyric files
eurovision = open("data/intersection.txt", "r", encoding='utf-8')
c60s = open("data/1960s.txt", "r", encoding ='utf-8')
c70s = open("data/1970s.txt", "r", encoding ='utf-8')
c80s = open("data/1980s.txt", "r", encoding ='utf-8')
c90s = open("data/1990s.txt", "r", encoding ='utf-8')
c00s = open("data/2000s.txt", "r", encoding ='utf-8')
c10s = open("data/2010s.txt", "r", encoding ='utf-8')

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

#split words into a list of its characters
def wordSplit(word): 
    return [char for char in word]  

#removes apostrophes in contractions
def removeConcat(text):
    strList = text.split()
    #splits string into words
    for i in range(len(strList)):
        #if a word has an apostrophe, split remove and concat
        if "'" in strList[i]:
            splitWord = wordSplit(strList[i])
            splitWord.remove("'")
            strList[i] = "".join(splitWord)
            
        #join string together 
        text = " ".join(strList)
        return text

#apply all functions to data
def cleanText(data):
    data = convLower(data)
    data = removePunctuation(data)
    data = removeNonAlphabet(data)
    data = removeNumbers(data)
    data = removeConcat(data)
    return data

#find artists in intersection.txt
def findArtist(artistName):
    with open("data/intersection.txt") as f:
        if artistName in f.read():
            return True

#read csv file of Eurovision songs metadata, store in dataframe
evMeta = pd.read_csv('data/EVmetadata.csv') 
evArtists = evMeta['Unnamed: 3']
evArtistList = evArtists.tolist()

#get column of artist names
evArtists = evMeta['Unnamed: 3']
evArtistList = evArtists.tolist()

#count how many artists are found in intersection.txt 
#to count how many songs are in the document
dcEV = 0
for i in range(len(evArtistList)):
    artistName = str(evArtistList[i])
    if findArtist(artistName) is True:
        dcEV = dcEV + 1 

#count how many documents are in the text file, marked by '-----'
#dcEV = eurovisionLyrics.count('-----')
dc60s = lyrics60s.count('-----')
dc70s = lyrics70s.count('-----')
dc80s = lyrics80s.count('-----')
dc90s = lyrics90s.count('-----')
dc00s = lyrics00s.count('-----')
dc10s = lyrics10s.count('-----')
dcTotal = dcEV + dc60s + dc70s + dc80s + dc90s + dc00s + dc10s 

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

