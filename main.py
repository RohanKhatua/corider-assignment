from flask import Flask, jsonify
from app.db import db
from app.routes.users import user_bp
from app.routes.ping import ping_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(ping_bp)


@app.route("/")
def index():
    try:
        db.command("ping")
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
