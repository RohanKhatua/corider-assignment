import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # MONGO_USERNAME = os.getenv("MONGO_DB_USERNAME")
    # MONGO_PASSWORD = os.getenv("MONGO_DB_PASSWORD")
    # MONGO_HOST = os.getenv("MONGO_DB_HOST", "localhost")
    # MONGO_PORT = os.getenv("MONGO_DB_PORT", 27017)
    # MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "test")
    # MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
    MONGO_URI = os.getenv("MONGO_URI")
