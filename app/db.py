from pymongo import MongoClient
from config import Config

try:
    client = MongoClient(Config.MONGO_URI)
    db = client[Config.MONGO_DB_NAME]
    print("Connected to MongoDB")
    print(db._name)
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    db = None
