from app.db import db
from bson.objectid import ObjectId
from app.schemas import UserSchema
from pydantic import ValidationError
import logging

log = logging.getLogger(__name__)


class UserModel:
    collection = db["users"]

    @staticmethod
    def create(data):
        try:
            user = UserSchema(**data)  # Validate the data using the schema
            user_id = UserModel.collection.insert_one(user.model_dump()).inserted_id
            return {"_id": str(user_id)}
        except ValidationError as e:
            # Handle validation error
            log.error(f"Validation error: {e}")
            return {"error": f"Validation error: {str(e)}"}
        except Exception as e:
            log.error(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def get_all(query=None, limit=None):
        try:
            # Initialize the query to an empty dictionary if none is provided
            query = query or {}

            # Create the base cursor
            cursor = UserModel.collection.find(query)

            # Apply limit if specified
            if limit:
                cursor = cursor.limit(limit)

            return cursor
        except Exception as e:
            # Handle exceptions
            log.error(f"An error occurred: {e}")
            return None

    @staticmethod
    def get_one(id):
        try:
            return UserModel.collection.find_one({"_id": ObjectId(id)})
        except Exception as e:
            # Handle exceptions
            log.error(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            user = UserSchema(**data)  # Validate the data using the schema
            # calling update_one with the filter and the update document
            updated_user = UserModel.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": user.model_dump()}
            )

            return updated_user
            # return {"_id": str(updated_user_id), "message": "User updated"}
        except ValidationError as e:
            # Handle validation error
            log.error(f"Validation error: {e}")
            return {"error": f"Validation error: {str(e)}"}
        except Exception as e:
            # Handle other exceptions such as database errors
            # Log the error
            log.error(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            return UserModel.collection.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            # Handle exceptions
            log.error(f"An error occurred: {e}")
            return {"error": str(e)}
