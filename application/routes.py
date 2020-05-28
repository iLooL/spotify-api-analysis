from application import app
from application.spotify import Spotify
import numpy as np
from flask import render_template, request, jsonify
import pickle

model = pickle.load(open('model.pkl', 'rb'))
spotify = Spotify()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/playlists', methods=['GET','POST'])
def playlists():
    user = request.form.get('username')
    playlists = spotify.getUserPlayList(user)
    print(playlists)
    return render_template('index.html', playlists=playlists)