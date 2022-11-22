from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from view import mainpage, addpage, makeplaylist, songinfopage
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.secret_key = '0000'

app.register_blueprint(mainpage.mainpage, url_prefix='/main')
app.register_blueprint(addpage.addpage, url_prefix='/addpage')
app.register_blueprint(makeplaylist.makeplaylist, url_prefix='/makeplaylist')
app.register_blueprint(songinfopage.songinfo, url_prefix='/songinfo')

@app.route('/')
def main():
    return render_template('main.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')