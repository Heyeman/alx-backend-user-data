#!/usr/bin/env python3
<<<<<<< HEAD
""" Flask app module
"""
from flask import Flask
from flask import jsonify, request, abort, redirect, make_response
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """ Return Json
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """ Register user
    """
    email = request.form.get('email', None)
    password = request.form.get('password', None)
=======
"""
Setup of a basic Flask app with various routes.
"""
from flask import Flask, jsonify, request,\
    abort, redirect, url_for, Response
from auth import Auth
from typing import Union

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """
    Home route
    Returns:
        str: Home page payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> Union[str, tuple]:
    """
    Register user route
    """
    email = request.form.get('email')
    password = request.form.get('password')
>>>>>>> 5efc399a590c1184beefcc242dacb7e62b03b8a9
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
<<<<<<< HEAD
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Login functionality
    """
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Logout and delete session
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ profile of logged in user
    """
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
=======
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Login user route. Creates a session_id cookie for the user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> Response:
    """
    Logout user route to delete the session_id cookie
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect(url_for('home'))


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> tuple:
    """
    Profile route to get user profile
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
>>>>>>> 5efc399a590c1184beefcc242dacb7e62b03b8a9
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
<<<<<<< HEAD
def get_reset_password_token():
    """ Generate reset token
    """
    email = request.form.get('email', None)
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token})
=======
def reset_password() -> tuple:
    """
    Reset password route to send a reset token to the user
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email,
                        "reset_token": token}), 200
>>>>>>> 5efc399a590c1184beefcc242dacb7e62b03b8a9
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
<<<<<<< HEAD
def update_password():
    """ Update password
    """
    email = request.form.get('email', None)
    reset_token = request.form.get('reset_token', None)
    password = request.form.get('new_password', None)
    try:
        AUTH.update_password(reset_token, password)
        return jsonify({"email": email, "message": "Password updated"})
=======
def update_password() -> tuple:
    """
    Update password route with reset token available in the request
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
>>>>>>> 5efc399a590c1184beefcc242dacb7e62b03b8a9
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
