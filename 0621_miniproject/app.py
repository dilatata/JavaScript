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

@app.route('/join', methods=["GET","POST"])
def join():
    if request.method == 'GET':
        return render_template('join.html')

    else:
        pass
		# ownerid = request.form.get('ownerid')
		# ownername = request.form.get('ownername')
		# password = request.form.get('password')
		# email = request.form.get('email')
        # address = request.form.get('address')
		# phoneno = request.form.get('phoneno')

		# if not (userid and username and password and re_password):
		# 	return "모두 입력해주세요"
		# elif password != re_password:
		# 	return "비밀번호를 확인해주세요"
		# else:
		# 	user = User()
		# 	user.password = password
		# 	user.userid = userid
		# 	user.username = username
		# 	db.session.add(user)
		# 	db.session.commit()
		# 	return "회원가입 완료"
		# return redirect('/')

@app.route('/login', methods=["POST"])
def login():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port='5000')