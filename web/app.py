from flask import Flask, jsonify, json, request
from flask_restful import Api, Resource
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

#client which connects to the database
client = MongoClient("mongodb://db:27017")

# Creating database named as "mydb"
db = client.mydb

#Inventory data has already been imported in 'inventory' collection inside 'mydb' database
#Getting all the inventories
@app.route('/inventoryAll', methods=['GET'])
def get_all_inventories():
    inventory = db.inventory

    output = []

    for q in inventory.find():
        output.append({'item' : q['item'], 'qty' : q['qty'], 'status' : q['status']})

    return jsonify({'result' : output})

#Quering for single inventory by item
@app.route('/inventoryOne/<item>', methods=['GET'])
def get_one_inventories(item):
    inventory = db.inventory

    q = inventory.find_one({'item': item})

    if q:
        output = {'item': q['item'], 'qty' : q['qty'], 'status' : q['status']}
    else:
        output = 'No results found'

    return jsonify({'result': output})

if __name__=="__main__":
	app.run(debug=True)







'''


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

# class startup(Resource):
# 	def get(self,id):
# 		cursor = db.inventory.find()
# 		#cursor = collection.find({"_id":id})
# 		return json.dump(cursor)

class startup(Resource):
	def get(self,id):
		output = []
		for data in db.inventory.find():
			output.append({"_id" : data['_id']})
		return jsonify({'result':output})


class startupall(Resource):
	def get(self):
		output = []
		for data in db.inventory.find():
			output.append({"item" : data['item']})

		return jsonify({'result':output})

class inventoryStatus(Resource):
	def get(self):
		output = []
		for data in db.inventory.find():
			output.append({"status" : data['status']})
		return jsonify({'result':output})

class inventoryIDs(Resource):
	def get(self):
		output = []
		for data in db.inventory.find():
                    return jsonify(data.inserted_ids)


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
api.add_resource(inventoryStatus, "/inventoryStatus")
api.add_resource(inventoryIDs, "/inventoryIDs")
# @app.route("/getstate")
# def get_state():
# 	for state in data['states']:
# 		return jsonify(state['name'])


'''