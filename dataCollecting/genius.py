"""
Gather lyrics with Genius API

This script is used to gather lyrics from Genius based on the data from Spotify

This script requires that 'pandas' and 'lyricsgenius'  be installed within the Python environment you are running this script in.
It also requires a Genius token that can be obtained from Genius (https://docs.genius.com/#/getting-started-h1)
as well as the csv files containing the chart data

This file can also be imported as a module and contains the following
functions: 
- removeHyphen: removes hyphen and all the characters after it 
- getLyrics: sends a get request to Genius to get lyrics
"""

import pandas as pd
import lyricsgenius 

from init import geniusToken

#read chart data
full1960s = pd.read_csv('chartData/1960s.csv')
full1970s = pd.read_csv('chartData/1970s.csv')
full1980s = pd.read_csv('chartData/1980s.csv')
full1990s = pd.read_csv('chartData/1990s.csv')
full2000s = pd.read_csv('chartData/2000s.csv')
full2010s = pd.read_csv('chartData/2010s.csv')
full1960s.drop(['Unnamed: 0'], axis=1)
full1970s.drop(['Unnamed: 0'], axis=1)
full1980s.drop(['Unnamed: 0'], axis=1)
full1990s.drop(['Unnamed: 0'], axis=1)
full2000s.drop(['Unnamed: 0'], axis=1)
full2010s.drop(['Unnamed: 0'], axis=1)

#get genius access token
genius = lyricsgenius.Genius(geniusToken(), skip_non_songs=True, remove_section_headers=True)

#clean data from Spotify to put into Genius
def removeHyphen(dfName):
    for index,row in dfName.iterrows():
        if "-" in row['name']: 
            dfName.at[index,'name'] = row['name'].split('-')[0].rstrip()

#get lyrics using Genius API by song title and artist name
def getLyrics(artistName, title):
    song = genius.search_song(title, artistName)
    return song.lyrics

#remove hyphens 
removeHyphen(full1960s)
removeHyphen(full1970s)
removeHyphen(full1980s)
removeHyphen(full1990s)
removeHyphen(full2000s)
removeHyphen(full2010s)

#get only the title of the song and the artist name
c1960s = full1960s[['name', 'artist']]
c1970s = full1970s[['name', 'artist']]
c1980s = full1980s[['name', 'artist']]
c1990s = full1990s[['name', 'artist']]
c2000s = full2000s[['name', 'artist']]
c2010s = full2010s[['name', 'artist']]

#write lyrics into text file
f = open("2010s.txt", "w") #not done due to timeout error
e = open("notFound.txt", "a") #doesnt work, titles added manually
count = 0

#look through dataframe of song titles and artist names
#search genius and get the lyrics
#write lyrics onto text file
for index, row in c2010s.iterrows():
    artist = row['artist']
    title = row['name']
    try:
        f.write(getLyrics(artist, title))
        count = count+1
        f.write("-----")
        print(count)
    except AttributeError:
        errorTitle = artist + ", " + title
        e.write(errorTitle)
        print("error: ", errorTitle)

f.close()
e.close()
