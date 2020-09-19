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

genius = lyricsgenius.Genius(geniusToken(), skip_non_songs=True, remove_section_headers=True)

def removeHyphen(dfName):
    for index,row in dfName.iterrows():
        if "-" in row['name']: 
            dfName.at[index,'name'] = row['name'].split('-')[0].rstrip()

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

c1960s = full1960s[['name', 'artist']]
c1970s = full1970s[['name', 'artist']]
c1980s = full1980s[['name', 'artist']]
c1990s = full1990s[['name', 'artist']]
c2000s = full2000s[['name', 'artist']]
c2010s = full2010s[['name', 'artist']]

f = open("1970s.txt", "w") #not done due to timeout error
e = open("notFound.txt", "w") #doesnt work, titles added manually
count = 0

for index, row in c1970s.iterrows():
    artist = row['artist']
    title = row['name']
    try:
        f.write(getLyrics(artist, title))
        count = count+1
        print(count)
    except AttributeError:
        errorTitle = artist + ", " + title
        e.write(errorTitle)
        print("error: ", errorTitle)

f.close()
e.close()
