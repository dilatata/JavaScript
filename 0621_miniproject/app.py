from flask import Flask, render_template, request
from flask.signals import request_finished
from dao import *
from dto import *

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@app.route('/join', methods=["POST"])
def join():
    dao = InfoDAO()
    dto = CustDTO(request.form.get('custid'), request.form.get('email'),  request.form.get('name'),  request.form.get('adress'),  request.form.get('phoneno'),  request.form.get('pw'))

    return dao.join(dto)

@app.route('/login', methods=["POST"])
def login():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')