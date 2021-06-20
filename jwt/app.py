from flask import Flask, jsonify, request, make_response
import jwt 
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretekey'

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token') #http//127.0.0.1:5000/route?token=skljfwoiefjksldfj
		if not token:
			return jsonify({'message':'Token is invalid'}), 403
		try: 
			data = jwt.decde(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message':'Token is invalid'}), 403
		return f(*args, **kwargs)
	
	return decorated


@app.route('/unprotected')
def unprotected(): #인증되지 않은 모두가 볼 수 있는
	return jsonify({'message':'Anyone can view this!'})


@app.route('/protected') #인증된 사람만 볼 수 있도록
@token_required
def protected():
	return jsonify({'message':'This is only avaliable for people with valid tokens.'})


@app.route('/login') #인증하지 못한 사람에게만 보이는 -> 인증된 사람은 볼 수 없게
def login():
	auth = request.authorization

	if auth and auth.password == 'secret':
		token = jwt.encode({'user':auth.username, 'exp':datetime. datetime.utcnow()+datetime.timedelta(minuts=30)}, app.config['SECRET_KEY'])

		return jsonify({'token': token.encode('UTF-8').decode('UTF-8')})

	return make_response('Could not verify!', 401, {'WWW-Autheniticate' : 'Basic real"Login Rquired"'})

#왜 /login 써도 password 치는 창이 안나오는거지?


if __name__ == '__main__':
	app.run(debug=True)