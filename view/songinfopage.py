from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist
from control.song_management import Song

songinfo = Blueprint('songinfo', __name__)

@songinfo.route('/<song_id>')
def songinfo_(song_id):
    song = Song.get_song(song_id)
    session['prev_page'] = request.referrer
    
    return render_template('songinfo.html', song_data=song)

@songinfo.route('/insert', methods=['POST'])
def songinsert():
    song_id = request.form['song_id']
    playlist_name = session['name']
    Playlist.add_song(Playlist.get_playlist_id(playlist_name)[0][0], song_id)
    print('추가완료')
    try:
        url = session['prev_page']
        print('try', url)
        session.pop('prev_page', None)
    except:
        url = '/addpage'
        print('except')
    return redirect(url)

@songinfo.route('/return_page', methods=['POST'])
def return_page():
    print('into return page')
    try:
        url = session['prev_page']
        print('try', url)
        session.pop('prev_page', None)
    except:
        url = '/addpage'
        print('except')
    return redirect(url)

