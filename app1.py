from flask import Flask, jsonify, json
app = Flask(__name__)

with open('states.json') as f:
	data = json.load(f)

@app.route("/")
def hello_world():
	return "Hello World"

@app.route("/bye")
def good_bye():
	json_dic = {
	'field1':'abc',
	'field2':'def'
	}
	return jsonify(json_dic)

@app.route("/getstate")
def get_state():
	for item in data['states']['name']:
		return jsonify(item)



if __name__=="__main__":
	app.run()
