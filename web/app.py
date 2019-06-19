from flask import Flask, jsonify, json, request
from flask_restful import Api, Resource
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

#client which connects to the database
client = MongoClient("mongodb://db:27017")

# database
db = client.mydb
# Created collection name: mycollection


# emp_rec1 = {
# 	        "name":"Mr.Geek",
# 	        "id":24,
# 	        "location":"delhi"
# 	        }
# emp_rec2 = {
# 	        "name":"Mr.Shaurya",
# 	        "id":14,
# 	        "location":"delhi"
# 	        }
#
# # Insert Data
# rec_id1 = collection.insert_one(emp_rec1)
# rec_id2 = collection.insert_one(emp_rec2)

class startup(Resource):
	def get(self,id):
		cursor = db.inventory.find()
		#cursor = collection.find({"_id":id})
		return json.dump(cursor)


class startupall(Resource):
	def get(self):
		output = []
		for data in db.inventory.find():
			output.append({"item" : data['item']})

		return jsonify({'result':output})

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

api.add_resource(startup, "/startup/<id>")
api.add_resource(startupall, "/startup/all")
# @app.route("/getstate")
# def get_state():
# 	for state in data['states']:
# 		return jsonify(state['name'])

if __name__=="__main__":
	app.run(host= '0.0.0.0')
