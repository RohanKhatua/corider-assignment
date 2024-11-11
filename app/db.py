from pymongo import MongoClient, errors
from config import Config
import logging

log = logging.getLogger(__name__)

# Declare db as None initially
db = None


def init_db():
    # log.debug("Initializing the database connection")
    global db  # Use the global db variable
    try:
        log.info("Connecting to MongoDB...")
        # log.info(f"Mongo URI: {Config.MONGO_URI}")
        client = MongoClient(
            Config.MONGO_URI, serverSelectionTimeoutMS=60000  # 1 minute timeout
        )
        client.server_info()  # Trigger connection attempt
        db = client.get_database("mydatabase")  # Set the database name
        log.info(f"Connected to MongoDB: {db._name}")
        return db
    except errors.ServerSelectionTimeoutError as e:
        # log.error("Error connecting to MongoDB: Connection timed out.")
        raise RuntimeError(f"Error connecting to MongoDB: {e}")
    except Exception as e:
        # log.error(f"Error connecting to MongoDB: {e}")
        raise RuntimeError(f"Error connecting to MongoDB: {e}")
