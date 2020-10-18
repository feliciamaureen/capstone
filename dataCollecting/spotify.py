"""
Gather chart data with Spotify API

This script is used to obtain chart data from Spotify playlists.

This script requires that 'pandas', 'requests', 'spotipy', and 'spotipy.oauth2' be installed within the Python environment you are running this script in.
It also requires a Spotify token that can be obtained from Spotify (https://developer.spotify.com/documentation/general/guides/authorization-guide/)

This file can also be imported as a module and contains the following
functions: 
- getTrackIDs: get the track IDs within a certain playlists
- getTrackFeatures: get all the information for each song in the playlists
"""

import requests
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

from init import spotifyAccess

#get spotify access token
sp = spotifyAccess()

#get list of track ID to retrieve data from playlist
def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

#get track
def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    #metadata
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    #features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

#list of spotify URIs: accessed 1 sept 2020
#60s = spotify:playlist:37i9dQZF1DXaKIA8E7WcJj
#70s = spotify:playlist:37i9dQZF1DWTJ7xPn4vNaz
#80s = spotify:playlist:37i9dQZF1DX4UtSsGT1Sbe 
#90s = spotify:playlist:37i9dQZF1DXbTxeAdrVG2l
#00s = spotify:playlist:37i9dQZF1DX4o1oenSJRJd
#10s = spotify:playlist:37i9dQZF1DX5Ejj0EkURtP

#get each track information and based on their ID from a playlist specified by the URI
ids = getTrackIDs('Spotify', '37i9dQZF1DX5Ejj0EkURtP')

tracks = []
for i in range(len(ids)):
    track = getTrackFeatures(ids[i])
    tracks.append(track)

#make dataframe with all obtained song information
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
fileName = '2010s' + ".csv"
#export dataframe to csv
df.to_csv(fileName, sep = ',')




