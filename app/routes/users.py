# main.py
from flask import Blueprint, request, jsonify
from app.models import UserModel
from bson.errors import InvalidId
from bson import json_util

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = UserModel.create(data)
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 201


@user_bp.route("/users", methods=["GET"])
def get_all_users():
    # print("Getting all users")
    result = list(UserModel.get_all())
    # print(f"Result: {result}")
    if "error" in result:
        return jsonify(result), 500

    # Convert ObjectId to string for each user document
    response = json_util.dumps(result)
    return response, 200, {"Content-Type": "application/json"}


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        result = UserModel.get_one(user_id)
        if not result:
            return jsonify({"error": "User not found"}), 404
        # result["_id"] = str(result["_id"])  # Convert ObjectId to string
        # return jsonify(result), 200
        response = json_util.dumps(result)
        return response, 200, {"Content-Type": "application/json"}
    except InvalidId:
        return jsonify({"error": "Invalid user ID format"}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    # print(f"Data: {data}")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        result = UserModel.update(user_id, data)
        # print("result was returned")
        if type(result) is dict and "error" in result:
            return jsonify(result), 400
        if result.matched_count == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User updated", "_id": f"{user_id}"}), 200
    except InvalidId:
        return jsonify({"error": "Invalid user ID format"}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


@user_bp.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        result = UserModel.delete(user_id)
        if result.deleted_count == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User deleted", "_id": user_id}), 200
    except InvalidId:
        return jsonify({"error": "Invalid user ID format"}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500
