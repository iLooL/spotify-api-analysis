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

    def getUserPlayList(self, user):
        playlists_data = self.sp.user_playlists(user)
    
        playlists = []
        for playlist_oject in playlists_data['items']:
            # playlist_name = playlist_oject['name']
            playlist_id = playlist_oject['name']
            playlists.append(playlist_id)
            # print(playlist_oject)
            # print(type(playlist_oject))

        
        return playlists
