from logging import DEBUG, info
from flask import Flask, request, render_template, jsonify
from flask.signals import request_finished
from flask_jwt_extended import *
import datetime
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
    dto = DogOwnerDTO(request.form.get("ownerid"), request.form.get("oewnername"), request.form.get("password"), request.form.get("email"), request.form.get("address"), request.form.get("phoneno"))
    dao.insertjoin(dto)

    return render_template('join.html')




app.config.update(
    DEBUG=True,
    JWT_SECRET_KEY="I'M IML"
)


jwt = JWTManager(app)



@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")



@app.route('/login', methods=['POST'])
def login_proc():

    user_id = request.form.get("ownerid")
    print('----- ', user_id)
    login_result = InfoDAO().login(request.form.get("ownerid"), request.form.get("password"))


    if login_result:
        print("--111----+++++ ",  login_result)

        return jsonify(result=200, access_token=create_access_token(identity=user_id))
    else:
        return jsonify(result="Invalid Params!")




@app.route('/booking', methods=["GET","POST"])
def booking():
    dao = InfoDAO()
    dto = BookDTO(request.form.get("bookingid"), request.form.get("ownerid"), request.form.get("roomno"),\
        request.form.get("bookingdate"), request.form.get("chindate"), request.form.get("choutdate"),\
            request.form.get("cancel"), request.form.get("dogname"), request.form.get("dogsize"),\
                request.form.get("dogbreed"), request.form.get("price"))
    dao.insertbook(dto)

    return render_template('booking.html')



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')