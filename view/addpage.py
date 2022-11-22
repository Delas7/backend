from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist
from control.song_management import Song

addpage = Blueprint('addpage', __name__)

@addpage.route('/')
def addpage_():
    return render_template('addsong.html')


# 곡명 검색
@addpage.route('/song', methods=['GET','POST'])
def song():
    if request.method == 'GET':
        name = request.args.get('song_name')
        song_list = Song.get_song(name)
        # print(song_list.get_song_title())
        # print(song_list.get_song_ids())
        song_data = []
        for i in range(len(song_list.get_song_title())):
            song_data.append([song_list.get_song_title()[i], song_list.get_song_ids()[i]])
        return render_template('addsong.html', playlist=song_data)
    else:
        print('else')
        return render_template('addsong.html')
    
# 각 곡별 상세정보
@addpage.route('/songinfo', methods=['GET'])
def songinfo():
    print('songdin')
    if request.method == 'GET':
        song_id = request.args.get('song_id')
    return render_template('songinfo.html', song_data = song_id)