from pymongo import MongoClient

client = MongoClient()
db = client.test
collection = db.cats
for cat in collection.find():
    print cat['name']