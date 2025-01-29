from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

email = "mohamedcali350@gmail.com"
github_url = "https://github.com/mohamedaliSwe/hng12-stage-0"


@app.route("/", methods = [ 'GET' ])
def get_info():
    response = {
        "email": email,
        "current_datetime": datetime.utcnow().isoformat(timespec="minutes"),
        "github_url": github_url
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run()
