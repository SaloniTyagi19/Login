from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/')
def form():
	return '''<form method="POST" action='/login' align="center">
	<table border="5dp" padding="5dp" margin="5dp" align="center" height="70%" width="60%">
	<tr><td colspan="2">
	<h3>Provide Username and Password</h3></td></tr>
	<tr><td><h3>Enter user name </h3></td>
	<td>
	<input type = 'text' name = 'uname'/></td></tr>
	<tr><td><h3>Enter Password </h3></td><td>
	<input type = 'text' name = 'pass'/></td></tr>
	<tr><td colspan="2" align="center"><input type = 'submit' value = 'Submit'/>
	</td></tr>
	</table>
	</form>'''
@app.route('/login',methods=['POST'])
def login():
	user_name = request.form['uname']
	pass1 = request.form['pass']
	if(user_name.isalpha() == True):
		if(len(pass1) < 6):
			return jsonify({'status' : 201, 'msg': "Failure: Password should be of length 6"})
		elif(pass1.isalpha() == True):
			return jsonify({'status': 202, 'msg': "Failure: password to have 1 character and 1 number"})
		else:
			return jsonify({'status': 200, 'msg': "Success"})
	else:
		return jsonify({'status': 203, 'msg': "Failure: only characters allowed in username"})
