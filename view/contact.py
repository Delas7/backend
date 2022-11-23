from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

contact = Blueprint('contact', __name__)

@contact.route('/')
def contact_():
    return render_template('contact.html')
