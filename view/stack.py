from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

stack = Blueprint('stack', __name__)

@stack.route('/')
def stack_():
    return render_template('stack.html')
