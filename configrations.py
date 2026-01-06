from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI", "mongodb+srv://vishalshinde4795:12345@cluster0.zu4i7b9.mongodb.net/?appName=Cluster0")
database_name = os.getenv("DATABASE_NAME", "todo_db")
collection_name = os.getenv("COLLECTION_NAME", "todo_data")

client = MongoClient(uri, server_api=ServerApi('1'))

db = client[database_name]
collection = db[collection_name]