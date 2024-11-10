from app.db import db
from bson.objectid import ObjectId
from app.schemas import UserSchema
from pydantic import ValidationError


class UserModel:
    collection = db["users"]

    @staticmethod
    def create(data):
        try:
            user = UserSchema(**data)
            user_id = UserModel.collection.insert_one(user.model_dump()).inserted_id
            return {"_id": str(user_id)}
        except ValidationError as e:
            # Handle validation error
            print(f"Validation error: {e}")
            return {"error": f"Validation error: {str(e)}"}
        except Exception as e:
            # Handle other exceptions such as database errors
            # Log the error
            print(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def get_all():
        try:
            return UserModel.collection.find()
        except Exception as e:
            # Handle exceptions
            print(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def get_one(id):
        try:
            return UserModel.collection.find_one({"_id": ObjectId(id)})
        except Exception as e:
            # Handle exceptions
            print(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        try:
            user = UserSchema(**data)
            updated_user = UserModel.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": user.model_dump()}
            )
            # print("user updated")
            # print(f"Updated user ID: {updated_user.upserted_id}")
            return updated_user
            # return {"_id": str(updated_user_id), "message": "User updated"}
        except ValidationError as e:
            # Handle validation error
            print(f"Validation error: {e}")
            return {"error": f"Validation error: {str(e)}"}
        except Exception as e:
            # Handle other exceptions such as database errors
            # Log the error
            print(f"An error occurred: {e}")
            return {"error": str(e)}

    @staticmethod
    def delete(id):
        try:
            return UserModel.collection.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            # Handle exceptions
            print(f"An error occurred: {e}")
            return {"error": str(e)}
