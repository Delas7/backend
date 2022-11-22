from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist


mainpage = Blueprint('main', __name__)

@mainpage.route('/')
def main():
    
    return render_template('main.html', playlist=['노래 %d'%(i) for i in range(30)], playlist_name = session['name'])

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
        print('GET')
        return redirect(url_for('main.main'))
    
    elif request.method == 'POST':
        print('POST')
        return render_template('makeplaylist.html')
    
    # elif request.method == 'DELETE':
        

# 곡 검색창 이동    
@mainpage.route('/addsong')
def addsong():
    print('to add song page')
    return render_template('addsong.html')

# 추천 곡 새로고침
@mainpage.route('/update-recommand')
def update_reconmmand():
    print('update recommand song')
    return redirect(url_for('main.main'))
