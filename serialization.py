from pymongo import MongoClient
import json
import jsonpickle
import time

def loadFromDB():
    
    stocks = []
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['stocks']
    
    results = coll.find({}, {'_id': 0})

    strValues = []
    
    for r in results:

        strValue = json.dumps(r)

        strValues.append(strValue)

    for str in strValues:
        
        obj = jsonpickle.decode(str)

        stocks.append(obj)

    return stocks