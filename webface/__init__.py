import flask
from flask_misaka import Misaka
app = flask.Flask(__name__)
app.secret_key = b'EEE, nejlepe os.urandom(24)'
Misaka(app)

from . import routes
