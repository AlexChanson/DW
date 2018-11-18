import spotipy
import sys
from pprint import pprint
import spotipy
import spotipy.util as util
import json
import csv
import requests



class CachedRequest:

    def __init__(self, clientID, clientSecret, ifAbsent):
        self.api_hits = 0
        self.cached = 0
        self.store = {}
        self.id = clientID
        self.secret = clientSecret
        self.func = ifAbsent
        self.token = util.oauth2.SpotifyClientCredentials(clientId, clientSecret)

        self.cache_token = self.token.get_access_token()
        self.sp = spotipy.Spotify(self.cache_token)
        #print(self.token)

    def request(self, id_: str):
        #print("ID requested",id_)
        if id_ in self.store.keys():
            self.cached += 1
            #print("We know it already", self.store[id_])
            return self.store[id_]
        else:
            self.api_hits += 1
            tmp = self.func(self.sp, id_)
            #print("Requested", tmp)
            self.store[id_] = tmp
            return tmp

    def refresh(self):
        self.token = util.oauth2.SpotifyClientCredentials(self.id, self.secret)
        self.sp = spotipy.Spotify(self.cache_token)

    def cache_ratio(self):
        return 1 - float(self.api_hits)/self.cached




############################
#       Parameterage       #
############################

clientId = "6bbad2bde89e4e3a9f497882353e2307"
clientSecret = "6858144db1174351af180a0899acc0bd"


def setup():
    def songrequest(apiObj, id):
        track = apiObj.track(id)
        return track
    songRequester = CachedRequest(clientId, clientSecret, songrequest)

    def artistrequester(apiObj, id):
        artist = apiObj.artist(id)
        return artist
    artistRequester = CachedRequest(clientId, clientSecret, artistrequester)

    def featurerequester(apiObj, id):
        track = apiObj.audio_features(id)
        return track
    featureRequester = CachedRequest(clientId, clientSecret, featurerequester)
    return songRequester, artistRequester, featureRequester



# Debut du script

song, artist, track = setup()



try:
    while True:
        mode_i = input("Enter mode [t]rack/[a]rtist/[f]eatures : ")
        mode = mode_i[0]
        if mode == "a":
            id = input("Input artist id : ")
            pprint(artist.request(id))
        elif mode == "t":
            id = input("Input track id : ")
            pprint(song.request(id))
        elif mode == "f":
            id = input("Input track id : ")
            pprint(track.request(id))
        else:
            print("Wrong mode '" + mode_i + "'")
except KeyboardInterrupt:
    print("Bye")

