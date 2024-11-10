from flask import Blueprint, jsonify
from db import db

ping_bp = Blueprint("ping_bp", __name__)


@ping_bp.route("/ping/db")
def index():
    try:
        db.command("ping")
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})


@ping_bp.route("/ping/app")
def index():
    return jsonify({"status": "ok"})
