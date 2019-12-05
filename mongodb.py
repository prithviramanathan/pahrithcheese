from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb')
db=client.pahrithcheese

c = "gouda"

result = db.available.find({ "cheese_name": c }, {"_id":0, "store_id": 1})


storeList = []

for r in result:
     storeList.append(r[store_id])

final = db.stores.find({ "store_id": {"$in": storeList} }, { "_id": 0, "store_name": 1, "address": 1})

pprint(final)