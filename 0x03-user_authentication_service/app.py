#!/usr/bin/env python3
"""flask_app
"""
from flask import Flask, jsonify, request
from auth import Auth
AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def test_app():
    """Flask app
        Return: ({"message": "Bienvenue"})
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def user():
    """Register user route

        getting email and passwod from the request body
        required fields: email, password
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Login Route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if not user:
            return Flask.abort, 401
    except Exception:
        return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
