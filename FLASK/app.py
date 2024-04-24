from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
import os
import secrets

app = Flask(__name__)

# Generate a random secret key for the Flask app
app.secret_key = secrets.token_hex(16)

# Use environment variables for MongoDB URI
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://mongodb:27017/Users')

mongo = PyMongo(app)
myclient = pymongo.MongoClient(app.config['MONGO_URI'])
mydb = myclient["Users"]
mycol = mydb["user"]

# Post method
@app.route('/add', methods=['POST'])    
def add_user():
    _json = request.json
    _name = _json.get('name')
    _email = _json.get('email')
    _password = _json.get('pwd')
    
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        mydict = {'name': _name, 'email': _email, 'pwd': _hashed_password} 
        x = mycol.insert_one(mydict)
        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route("/users", methods=['GET'])
def users():
    users = mycol.find()
    resp = dumps(users)
    return resp  

# Put method
@app.route("/updateUser", methods=['PUT'])
def updateUser():
    _json = request.json
    _name = _json.get('name')
    if _name:
        myquery = { "name": { "$regex": _name } }
        newvalues = { "$set": { "name": "_"+_name } }
        x = mycol.update_many(myquery, newvalues)
        resp = "Updated Successfully"
        return resp
    else:
        return not_found()

# delete method
@app.route("/deleteUser", methods=['DELETE'])
def deleteUser():
    _json = request.json
    _name = _json.get('name')
    if _name:
        myquery = { "name": _name }
        mycol.delete_one(myquery)
        resp = _name + " deleted Successfully"
        return resp    
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message' : 'Not Found' + request.url 
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
