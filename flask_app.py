from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/",methods=['POST'])
def index():	
	fname,lname = request.get_json().values()
	return jsonify({'status':True,'fullname':fname+" "+lname})

if __name__=='__main__':	
	app.run(debug=True,port=8080)