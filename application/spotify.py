import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'debb421555db4be0b8df8639bed56306'
secret = 'a352e458606b421fb51c7cbafc329f88'

class Spotify():
    def __init__(self):
        # initialize all variables
        self.user = ''
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        self.sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    def setUser(self, user):
        self.user = user

    # gets playlist name, id and image
    def getUserPlaylists(self):
        playlists_data = self.sp.user_playlists(self.user)
        playlists = {}
        
        for playlist_object in playlists_data['items']:
            id = playlist_object['id']
            name = playlist_object['name']
            playlists[name] = id

        print(playlists)

        return playlists
