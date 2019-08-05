from flask import request,jsonify
from app import app
import json


@app.route('/allcategories',methods = ['GET'])
def allcategory():
    if request.method == 'GET':

        with open('categories.json') as json_file:
            data = json.load(json_file)
        
        
        response = jsonify(data)        
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response