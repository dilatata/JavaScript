from logging import DEBUG
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




# 여기서부터 jwt로그인
app.config.update(
    DEBUG=True,
    JWT_SECRET_KEY="I'M IML"
)

jwt = JWTManager(app)

# admin_id = "tester"
# admin_pw = "11"


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_proc():
    user_id = request.form.get("id")
    user_pw = request.form.get("pw")

    dao = InfoDAO()
    dto = DogOwnerDTO(request.form.get("ownerid"), request.form.get("password"))
    dao.login(dto)

    admin_id = jsonify(dao.login("ownerid"))
    admin_pw = jsonify(dao.login("password"))

    if (user_id == admin_id and user_pw == admin_pw):
        return jsonify(result=200, access_token=create_access_token(identity=user_id))
    else:
        return jsonify(result="Invalid Params!")


@app.route("/jwtconfirm")
@jwt_required()   # 참조 사이트에선 () 표현이 누락, 즉 버전에 따른 차이
def jwt_confirm():
    cur_user = get_jwt_identity()
    print(cur_user)
    return '{"id":"' + cur_user + '"}'




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')