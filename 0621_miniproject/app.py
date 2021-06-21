from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@app.route('/join', methodes=["POST"])
def join():
    dao = InfoDAO()