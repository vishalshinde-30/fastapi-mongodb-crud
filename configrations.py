
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://vishalshinde4795:12345@cluster0.zu4i7b9.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db  =  client.todo_db
collection  =  db["todo_data"]