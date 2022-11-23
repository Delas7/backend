from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.playlist_management import Playlist

main1 = Blueprint('main1', __name__)

@main1.route('/')
def main1_():
    return render_template('main1.html')
