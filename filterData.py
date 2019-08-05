from flask import request ,jsonify
import json
from app import app


  

@app.route('/filterData',methods = ['POST'])
def filterData():
    if request.method == 'POST':

            payload=request.get_json()
            filterdata=[]
            with open('amazon.json') as json_file:
                data = json.load(json_file)
           
            for i in data:
                if list(payload.values()).pop()==i[list(payload.keys()).pop()]:
                    filterdata.append(i)
            
            with open('flipkart.json') as json_file:
                data = json.load(json_file)
           
            for i in data:
                if list(payload.values()).pop()==i[list(payload.keys()).pop()]:
                    filterdata.append(i)
            



            response = jsonify(filterdata)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
            
        








