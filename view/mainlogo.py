from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist


mainlogo = Blueprint('mainlogo', __name__)

# mainlogo page
@mainlogo.route('/')
def main():
    return render_template('mainLogo.html')
