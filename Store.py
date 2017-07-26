from os import walk
from load import getLines, formatData
from pymongo import MongoClient
import json
import jsonpickle

mypath = '/home/ky/Desktop/export/'

f = []

for (dirpath, dirname, filenames) in walk(mypath):
    
    f.extend(filenames)

print(f)

stocks = []

for file in f:

    filePath = mypath + file

    stocks.append(formatData(getLines(filePath)))

client = MongoClient('localhost', 27017)

db = client["test"]

coll = db['stocks']

jsons = []

v = json.loads(jsonpickle.encode(stocks))

# forozen = json.dumps(v, indent=len(stocks))

coll.insert_many(v)