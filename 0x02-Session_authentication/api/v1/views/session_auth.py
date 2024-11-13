#!/usr/bin/env python3
""" Session authentication view"""
from api.v1.views import app_views
import os
from flask import jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - Dictionary representation of the User
    """
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    user = users[0]
    session_id = auth.create_session(user.id)
    user_json = jsonify(user.to_json())
    SESSION_NAME = os.getenv('SESSION_NAME')
    user_json.set_cookie(SESSION_NAME, session_id)
    return user_json


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - Empty dictionary
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
