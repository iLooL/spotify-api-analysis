import spotipy
import requests
from bs4 import BeautifulSoup
from googlesearch import search
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

        return playlists

    def getPlaylistTracks(self, playlist_id):
        """
        Arguments:
            playlist_id {[string]} -- takes in a spotify playlist_id
            that the user has in their library

        Returns:
            playlist_tracks {[list]} -- has every songs artist, song name
            and song id from a given playlist
        """
        response = self.sp.user_playlist_tracks(self.user, playlist_id)
        playlist_tracks = response["items"]
        # maybe change this to a dictionary?
        all_tracks = []
        
        # get all songs from playlist
        # spotipy has a limit of 100 songs per API call
        while len(playlist_tracks) < response["total"]:
            response = sp.user_playlist_tracks(user, playlist_id, offset=len(playlist_tracks))
            playlist_tracks.extend(response["items"])
            
        # test case to make sure we have the correct number of tracks
        # print(len(playlist_tracks) == response["total"])
        
        for track in playlist_tracks:
            # line below prints the response well
            # print(json.dumps(t["track"], indent=2))

            artist = track["track"]["artists"][0]['name']
            track_name = track["track"]["name"]
            track_id = track["track"]["id"]
            all_tracks.append([artist, track_name, track_id])

        return all_tracks

    def getPlaylistLyrics(self, playlist_songs):
    
        lyrics = []
        
        for song in playlist_songs:
            # .join() method is fast than regular string concatentation
            query_sequence = (song[0], song[1], 'lyrics')
            search_query = ' '.join(query_sequence)

            for web_page in search(search_query, tld="com", num=10, stop=10, pause=2): 
                if 'azlyrics' in web_page:
                    break

            try:
                URL = web_page
                webpage = requests.get(URL)
                soup = BeautifulSoup(webpage.content, 'html.parser')
                print(search_query)
                testing = soup.find('div', {'class': ''}).text
                lyrics.append(testing)
            except AttributeError as err:
                print("Website was not found for " + search_query)
            except ConnectionError as err:
                print("Connection error for " + search_query)
        return lyrics

