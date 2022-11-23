from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

makeplaylist = Blueprint('makepalylist', __name__)

@makeplaylist.route('/')
def makeplaylist_():
    return render_template('makeplaylist.html')

# 플레이리스트 추가 메서드
@makeplaylist.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['playlistname']
        ratio = request.form['ratio']
        
        if name and ratio:
           Playlist.make_new_playlist(name, ratio)
    
    session['name'] = name
    return redirect(url_for('main.main'))

@makeplaylist.route('/cancel')
def cancel():
    return redirect(url_for('main.main'))