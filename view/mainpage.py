from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist


mainpage = Blueprint('main', __name__)

@mainpage.route('/')
def main():
    # 전체 플레이리스트 조회
    
    playlist_data = Playlist.get_playlist_id()
    playlist_names = []
    for el in playlist_data:
        playlist_names.append(el[1])
        
    # 세션 정보(현재 플레이리스트 이름) 조회
    try:
        session_name = session['name']
    except:
        session_name = None
    print(session_name)
    if not session_name:
        return render_template('main.html', total_list=playlist_names)
   

    
    # 현재 플레이리스트의 곡 목록
    playlist_songs = []
    try:
        session_name_id = Playlist.get_playlist_id(session_name)[0][0]
        if session_name:
            for el in Playlist.get(session_name_id).get_songlist():
                playlist_songs.append(el)
    except:
        pass
        
        
    return render_template('main.html', 
                           playlist=playlist_songs,
                           playlist_name = session_name,
                           total_list=playlist_names)

# 플레이리스트 선택, 추가, 제거
@mainpage.route('/playlist', methods=['GET', 'POST', 'DELETE'])
def playlist():
    if request.args.get('_method') == 'DELETE':
        print('DELETE')
        playlist_name = request.args.get('playlist_name')
        try:
            Playlist.delete_playlist(playlist_name)
            session['name'] = None
        except:
            pass
        return redirect(url_for('main.main'))

    if request.method == 'GET':
        playlist_name = request.args.get('playlist')
        session['name'] = playlist_name
        print('GET')
        return redirect(url_for('main.main'))
    
    elif request.method == 'POST':
        print('POST')
        return render_template('makeplaylist.html')
    
    # elif request.method == 'DELETE':
        

# 추천 곡 새로고침
@mainpage.route('/update-recommand')
def update_reconmmand():
    print('update recommand song')
    return redirect(url_for('main.main'))
