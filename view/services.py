from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

services = Blueprint('services', __name__)

@services.route('/')
def services_():
    return render_template('services.html')
