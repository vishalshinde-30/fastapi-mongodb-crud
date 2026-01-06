from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv


load_dotenv('.env.local')  
load_dotenv()  

uri = os.getenv("MONGODB_URI")

if not uri:
    raise ValueError("""
    MONGODB_URI environment variable is not set.
    
    Please create a .env file with:
    MONGODB_URI=your_mongodb_connection_string
    DATABASE_NAME=todo_db
    COLLECTION_NAME=todo_data
    
    Or if developing locally, create .env.local with your credentials.
    """)

database_name = os.getenv("DATABASE_NAME", "todo_db")
collection_name = os.getenv("COLLECTION_NAME", "todo_data")

client = MongoClient(uri, server_api=ServerApi('1'))

db = client[database_name]
collection = db[collection_name]