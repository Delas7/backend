from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

team = Blueprint('team', __name__)

@team.route('/')
def team_():
    return render_template('team.html')
