from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

about_us = Blueprint('about_us', __name__)

@about_us.route('/')
def about_us_():
    return render_template('about_us.html')
