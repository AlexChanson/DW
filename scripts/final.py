import spotipy
import sys
import pprint
import spotipy
import spotipy.util as util
import json
import csv


class CachedRequest:

    def __init__(self, clientID, clientSecret, ifAbsent):
        self.store = {}
        self.id = clientID
        self.secret = clientSecret
        self.func = ifAbsent
        self.token = util.oauth2.SpotifyClientCredentials(clientId, clientSecret)

        self.cache_token = self.token.get_access_token()
        self.sp = spotipy.Spotify(self.cache_token)
        #print(self.token)

    def request(self, id_: str):
        print("ID requested",id_)
        if id_ in self.store.keys():
            print("We know it already", self.store[id_])
            return self.store[id_]
        else:
            tmp = self.func(self.sp, id_)
            print("Requested", tmp)
            self.store[id_] = tmp
            return tmp

    def refresh(self):
        self.token = util.oauth2.SpotifyClientCredentials(self.id, self.secret)
        self.sp = spotipy.Spotify(self.cache_token)

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

def addattributes(input, songRequester, artistRequester, featureRequester):

    id = input[31:]
    print(input)


    urn = 'spotify:track:' + id
    track = songRequester.request(urn)
    trackpopularity = track["popularity"]

    # valuename = track['artists'][0]['id']
    # valuename2 = sp.artist('spotify:artist:' + valuename)
    # artistname = valuename2['name']

    valuefollow = track['artists'][0]['id']
    follow2 = artistRequester.request('spotify:artist:' + valuefollow)
    followers = follow2['followers']['total']

    id = track['artists'][0]['id']  # trouve le nom de l'artiste
    artistpopularity = artistRequester.request(id)['popularity']

    # albumname = track['album']['name']

    value = track['artists'][0]['id']
    value2 = artistRequester.request('spotify:artist:' + value)
    value3 = value2['genres']

    try:
        artistgenre = value3[0]
    except IndexError:
        artistgenre = "other"

    releasedate = track['album']['release_date']

    audiofeatures = featureRequester.request(urn)

    tempo = audiofeatures[0]['tempo']

    danceability = audiofeatures[0]['danceability']

    length = audiofeatures[0]['duration_ms']

    return [str(trackpopularity), str(followers), str(artistpopularity), artistgenre, str(releasedate), str(tempo),
            str(danceability), str(length)]

def cleanup():
    pass

# Debut du script


# Parameterage
infile = "cleandata.csv"
outfile = "datafinal.csv"
separateur = ";"
header = True

song, artist, track = setup()

with open(infile, encoding='utf8') as f:
    lines = csv.reader(f, delimiter=separateur)
    with open(outfile, encoding='utf8', mode="w") as out:
        for line in lines:
            if header:
                header = False
                out.write(separateur.join(line) + "\n")
            else:
                result = addattributes(line[len(line) - 3], song, artist, track)
                out.write(separateur.join(line))
                for item in result:
                    out.write(separateur + item)
                out.write("\n")
        cleanup()


