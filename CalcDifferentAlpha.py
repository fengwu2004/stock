import serialization
from wave_strategy import WaveStrategyUnit
import jsonpickle
from pymongo import MongoClient
import json

stocks = serialization.loadFromDB()

results = []

alpha = 0.08

for stock in stocks:
    
    wavaUnit = WaveStrategyUnit(stock, alpha)
    
    results.append(wavaUnit)

def save():
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    name = "alpha_%s" % alpha
    
    coll = db[name]
    
    v = json.loads(jsonpickle.encode(results))
    
    coll.insert_many(v)
    
save()