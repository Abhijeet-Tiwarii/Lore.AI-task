from flask import Flask, jsonify, json, request
from flask_restful import Api, Resource
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

#client which connects to the database
client = MongoClient("mongodb://db:27017")
db = client.aNewDB
statescollec = db["statescollec"]
#upload dataset
#into aNewDB (database) inside
#statescollec (colllection)

class Statesname(Resource):
	def get(self):
		state_name = statescollec.find({})[0]['states']
		return (state_name)

# class State(Resource):
# 	def get(self):
# 		#query with db and collection name
# 	retSt =	statsdb.statesCollection.find(
# 	{states[name]}
# 	)

		# get the states from the statesdb database and statesCollection collection
#		return jsonify(retSt)


# with open('states.json') as f:
# 	data = json.load(f)

#for testing
@app.route("/")
def hello_world():
	return "Hello World"

#for testing
@app.route("/bye")
def good_bye():
	json_dic = {
	'field1':'abc',
	'field2':'def'
	}
	return jsonify(json_dic)

api.add_resource(Statesname, "/state")
# @app.route("/getstate")
# def get_state():
# 	for state in data['states']:
# 		return jsonify(state['name'])

if __name__=="__main__":
	app.run(host= '0.0.0.0')
