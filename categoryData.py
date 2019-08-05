from flask import request ,jsonify
import json
from app import app


  

@app.route('/categoryData',methods = ['GET'])
def categoryData():
    if request.method == 'GET':
            alldata=[]
            with open('amazon.json') as json_file:
                data = json.load(json_file)

            amazon={"amazon":data}
            alldata.append(amazon)
            with open('flipkart.json') as json_file:
                data = json.load(json_file)

            flipkart={"flipkart":data}
            alldata.append(flipkart)

            response = jsonify(alldata)        
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
            
        








