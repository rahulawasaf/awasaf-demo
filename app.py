import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD with Docker is working!"

if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    app.run(host=host, port=5000)
