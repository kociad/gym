import flask

app=flask.Flask(__name__)
app.secret_key=b'EEE, nejlepe os.urandom(24)'