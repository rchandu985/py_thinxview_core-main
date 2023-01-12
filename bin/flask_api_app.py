from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from bin.test import o
import json

app = Flask(__name__)

api = Api(app)
  
class Testing(Resource):
  
   
    
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        
        print(o(data['data'],data['device_id']))
        return jsonify(data)


api.add_resource(Testing, '/')
if __name__ == '__main__':
    app.run(debug=True)