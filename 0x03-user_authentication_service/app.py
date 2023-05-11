#!/usr/bin/env python3
"""flask_app
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth
AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Flask app
        Return: ({"message": "Bienvenue"})
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """Register user route

        getting email and passwod from the request body
        required fields: email, password
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        if new_user is not None:
            return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Login Route
        valid_login: emil, password
        for login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    # valid_login = AUTH.valid_login(email, password)

    # if not valid_login:
    #     abort(400)
    if not AUTH.valid_login(email, password):
       abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response

@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout route
        destroy_session: user_id
        Response to : DELETE/sessions
    """
    cookies = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(cookies)
    if user is None or cookies is None:
        abort(403)
    else:
        if user:
            AUTH.destroy_session(user.id)
            return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
