import pymongo
import os
from dotenv import load_dotenv
#from datetime import datetime
load_dotenv()
MONGO_USER = os.getenv("MONGO_USER", default="OOPS")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
MONGO_CLUSTER= os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
print("----------------")
connection_uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.mongodb.net/test?retryWrites=true&w=majority"
print("URI:", connection_uri)
print("----------------")
client = pymongo.MongoClient(connection_uri)
print("CLIENT:", type(client), client)
print("----------------")
db = client.another_test_database
print("DB:", type(db), db)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())
print("----------------")
collection = db.pokemon
print("COLLECTION:", type(collection), collection)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())
pika = {
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "some_other_key": 1098
}
collection.insert_one(pika)
#
# INSERTS
#
mewtwo = {
    "name": "Mewtwo",
    "level": 100,
    "exp": 76000000000,
    "hp": 450,
    "strength": 550,
    "intelligence": 450,
    "dexterity": 300,
    "wisdom": 575
}
pikachu = {
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
}
blastoise = {
    "name": "Blastoise",
    "lvl": 70,
}
characters = [mewtwo, pikachu, blastoise]
print("INSERT ONE AT A TIME...")
for character in characters:
    print(character["name"])
    collection.insert_one(character)
print("----------------")
print("COUNT ALL DOCUMENTS:")
print(collection.count_documents({}))
print("COUNT ALL PIKACHUS:")
print(collection.count_documents({"name": "Pikachu"}))