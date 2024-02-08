import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

# Create Connection
def createConnection():
    uri = os.getenv("DB_URI")
    db = os.getenv("DB_NAME")
    collection = os.getenv("DB_COLLECTION")

    try:
        myClient = pymongo.MongoClient(uri)

        db = myClient[db]
        collection = db[collection]
        return collection
    
    except pymongo.errors.ConnectionFailure as error:
        print(f"Error connecting to MongoDB: {error}")
        return None
    

# Close Connection
def closeConnection(myClient):
    try:
        myClient.close()
    except pymongo.errors.ConnectionFailure as error:
        print(error)    

# Create Function
def create(name, address):
    try:
        collection = createConnection()
        newRecord = {"name": name, "address": address}
        collection.insert_one(newRecord)
        print(f"Record for {name} inserted successfully!")
    except pymongo.errors.ConnectionFailure as error:
        print(error)

# Read All Function
def readAll():
    try:
        collection = createConnection()
        for record in collection.find({},{"_id": 0, "name": 1, "address": 1}):
            print(record)
    except pymongo.errors.ConnectionFailure as error:
        print(error)

# Search By Name Function
def searchByName(name):
    try:
        collection = createConnection()

        query = {"name": name}

        for record in collection.find(query,{"_id": 0, "name": 1, "address": 1}):
            print(record)
    except pymongo.errors.ConnectionFailure as error:
        print(error)

# Update Function
def update(oldName, newName, newAddress):
    try:
        collection = createConnection()
        collection.update_one({"name": oldName}, {"$set": {"name": newName, "address": newAddress}})
        print(f"Record for {oldName} updated successfully!")
    except pymongo.errors.ConnectionFailure as error:
        print(error)

# Delete Function
def delete(name):
    try:
        collection = createConnection()
        collection.delete_one({"name": name})
        print(f"Record for {name} deleted successfully!")
    except pymongo.errors.ConnectionFailure as error:
        print(error)