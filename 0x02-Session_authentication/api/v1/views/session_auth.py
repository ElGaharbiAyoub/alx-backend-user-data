#!/usr/bin/env python3
""" Module session_auth
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from typing import TypeVar
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
      - 400 if the User doesn't exist
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if user is None or user == []:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return response


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - empty JSON if the session has been correctly deleted
    """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
