from flask import Flask
from flask_cors import CORS

api = Flask(__name__)
CORS(api)


@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
        "dob": "31/07/2001"
    }

    return response_body


api.run(host="localhost", port=54321, debug=True)
