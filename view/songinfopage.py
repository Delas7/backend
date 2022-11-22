from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist
from control.song_management import Song

songinfo = Blueprint('songinfo', __name__)

@songinfo.route('/<song_id>')
def songinfo_(song_id):
    song = Song.get_song(song_id)
    
    return render_template('songinfo.html', song_data=song)

@songinfo.route('/insert', methods=['POST'])
def songinsert():
    song_id = request.form['song_id']
    url = 'songinfo.songinfo_'
    # try:
    playlist_name = session['name']
    Playlist.add_song(Playlist.get_playlist_id(playlist_name), song_id)
    print('cp2')
    print('추가완료')
    # except:
    #     print('추가안됨')
    return redirect(url_for(url, song_id=song_id))

