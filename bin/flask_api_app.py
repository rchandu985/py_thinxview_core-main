from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from bin.test import o
import json
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.

class Testing(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        
        print(o(data['data']))
        return jsonify(data)


api.add_resource(Testing, '/')
if __name__ == '__main__':
    app.run(debug=True)