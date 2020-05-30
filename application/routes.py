from application import app
from application.spotify import Spotify
import numpy as np
from flask import render_template, request, jsonify
import pickle

model = pickle.load(open('model.pkl', 'rb'))
spotify = Spotify()
playlists = ''

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/playlists', methods=['GET','POST'])
def playlists():
    # get and set the username
    user = request.form.get('username')
    spotify.setUser(user)

    # get information for playlist display
    playlists = spotify.getUserPlaylists()

    return render_template('index.html', playlists=playlists)

@app.route('/playlists/<playlistId>')
def playlist_info(playlistId):
    
    playlist_songs = spotify.getPlaylistTracks(playlistId)
    playlist_lyrics = spotify.getPlaylistLyrics(playlist_songs)

    return render_template("playlist-info.html", playlist_songs=playlist_songs, playlist_lyrics=playlist_lyrics)