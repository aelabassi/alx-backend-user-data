#!/usr/bin/env python3
""" Auth module"""
from flask import request
import os
from typing import List, TypeVar, Union


class Auth:
    """ Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        tmp_path = path
        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path[-1] != '*':
                if tmp_path == excluded_path:
                    return False
            else:
                if excluded_path[:-1] == path[:len(excluded_path) - 1]:
                    return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        return None

    def session_cookie(self, request=None):
        """ session_cookie method
        """
        SESSION_NAME = os.getenv('SESSION_NAME')
        if request is None:
            return None
        session_name = request.cookies.get(SESSION_NAME)
        return session_name
