# main.py
from flask import Blueprint, request, jsonify
from app.models import UserModel
from bson.errors import InvalidId
from bson import ObjectId, json_util

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
    try:
        # Get cursor and per_page parameters from query string
        cursor_id = request.args.get("cursor")
        per_page = int(request.args.get("per_page", 10))

        # Build query for cursor-based pagination
        query = {}
        if cursor_id:
            query["_id"] = {"$gt": ObjectId(cursor_id)}

        # Fetch the users with cursor-based pagination
        cursor = UserModel.get_all(query=query, limit=per_page)
        result = list(cursor)

        # Prepare the next cursor
        next_cursor = result[-1]["_id"] if result else None

        # Convert ObjectId to string for each user document
        response_data = {
            "users": json_util.loads(json_util.dumps(result)),
            "next_cursor": str(next_cursor) if next_cursor else None,
        }

        return json_util.dumps(response_data), 200, {"Content-Type": "application/json"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


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
