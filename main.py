from flask import Flask, jsonify, request, render_template, make_response, session, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
import os
from view import mainlogo, main1, about_us, contact, pricing, services, stack, team, all_music

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.secret_key = '1'

app.register_blueprint(mainlogo.mainlogo, url_prefix='/mainlogo')
app.register_blueprint(main1.main1, url_prefix='/main1')
app.register_blueprint(about_us.about_us, url_prefix='/about_us')
app.register_blueprint(contact.contact, url_prefix='/contact')
app.register_blueprint(pricing.pricing, url_prefix='/pricing')
app.register_blueprint(services.services, url_prefix='/services')
app.register_blueprint(stack.stack, url_prefix='/stack')
app.register_blueprint(team.team, url_prefix='/team')
app.register_blueprint(all_music.all_music, url_prefix='/all_music')


@app.route('/')
def main():
    return redirect(url_for('mainlogo.main'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')