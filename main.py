import logging
import sys
from app.db import init_db  # Import db so other files can access it
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)
logging.getLogger("pymongo").setLevel(logging.WARNING)

# Run the database check before the app starts
try:
    log.debug("Calling init_db() from main.py")
    init_db()  # Initialize the database; this sets the db object in db.py
except RuntimeError as e:
    sys.exit(str(e))  # Exit the app with an error if the DB check fails

from flask import Flask
from app.routes.users import user_bp
from app.routes.ping import ping_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(ping_bp)


if __name__ == "__main__":
    print("Starting the app")
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT")), debug=True)
