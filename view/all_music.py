from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist
from control.song_management import Song
import math

all_music = Blueprint('all_music', __name__)

# allmusic page
@all_music.route('/')
def all_music_():
    return render_template('all_music.html')


@all_music.route('/search', methods=['POST', 'GET'])
def search():
    print(request.method)
    if request.method == 'GET':
        keyword = request.args.get('search_keyword')
        song_list = Song.get_song(keyword)
        song_data = []
        for i in range(len(song_list.get_song_title())):
            song_data.append([song_list.get_song_title()[i], song_list.get_song_ids()[i]])
        
        page = request.args.get('page', 1, type=int)    
        limit = 10
        
        datas = song_data[(page-1)*limit : page * limit]
        total_count = len(song_data)
        last_page_num = math.ceil(total_count / limit)

        block_size = 5
        block_num = int((page-1) / block_size)
        block_start = (block_size * block_num) + 1
        block_end = block_start + (block_size - 1)
        
        return render_template('all_music.html',
                               playlist=datas,
                               search_keyword = keyword,
                               block_start=block_start,
                               block_end=block_end,
                               page=page,
                               last_page_num=last_page_num,
                               )
        
        