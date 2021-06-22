from flask import Flask, render_template, request
from flask.signals import request_finished
from dao import *
from dto import *

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')



@app.route('/join', methods=['GET','POST'])
def join():
    
    dao = InfoDAO()
    dto = DogOwnerDTO(request.form.get("ownerid"), request.form.get("oewnername"), request.form.get("password"), request.form.get("email"), request.form.get("address"), request.form.get("phoneno"), request.form.get("accumpoints"))
    dao.insertjoin(dto)

    return render_template('join.html')



@app.route('/login', methods=["POST"])
def login():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')