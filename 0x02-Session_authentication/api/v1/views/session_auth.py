#!/usr/bin/env python3
"""view for Session Authentication
"""
from os import getenv
from flask import Flask, jsonify, make_response
from flask import request
from models.user import User
from api.v1.views import app_views
app = Flask(__name__)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Login Route"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400

    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({'email': email})
        if not user:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    user_obj = user[0]
    if not user_obj.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user_id = user_obj.id
    # creating New session id for the user
    session_id = auth.create_session(user_id)
    # return the obj to json string
    user_json = user_obj.to_json()
    # setting cookie to the response
    response = make_response(user_json)
    session_cookie = getenv('SESSION_NAME')
    response.set_cookie(session_cookie, session_id)
    return response
