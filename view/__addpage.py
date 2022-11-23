from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist
from control.song_management import Song
import math

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
        song_data = []
        for i in range(len(song_list.get_song_title())):
            song_data.append([song_list.get_song_title()[i], song_list.get_song_ids()[i]])
        
        page = request.args.get('page', 1, type=int)    
        limit = 1
        
        datas = song_data[(page-1)*limit : page * limit]
        total_count = len(song_data)
        last_page_num = math.ceil(total_count / limit)

        block_size = 5
        block_num = int((page-1) / block_size)
        block_start = (block_size * block_num) + 1
        block_end = block_start + (block_size - 1)
        
        return render_template('addsong.html',
                               playlist=datas,
                               search_keyword = name,
                               block_start=block_start,
                               block_end=block_end,
                               page=page,
                               last_page_num=last_page_num,
                               )
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


@addpage.route('/list')
def song_list():
    pass