from pymongo import MongoClient
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.pahrithcheese

c = "Gouda"

result = db.available.find({ "cheese_name": c }, {"_id":0, "store_id": 1})

storeList = []
for r in result:
     storeList.append(r["store_id"])

final = list(db.stores.find({ "store_id": {"$in": storeList} }, { "_id": 0, "store_name": 1, "address": 1}))

pprint(final)
