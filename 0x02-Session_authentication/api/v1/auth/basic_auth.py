#!/usr/bin/env python3
""" Basic authentication module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header method
        """
        if authorization_header is None or \
           type(authorization_header) is not str or \
           not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """ decode_base64_authorization_header method
        """
        if base64_authorization_header is None or \
           not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded = b64decode(encoded)
            decoded = decoded.decode('utf-8')
        except Exception:
            return None
        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)\
            -> (str, str):
        """ extract_user_credentials method
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str) or \
           ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str)\
            -> User:
        """ user_object_from_credentials method """
        if user_email is None or user_pwd is None or\
            not isinstance(user_email, str)\
                or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        encoded = self.extract_base64_authorization_header(auth_header)
        if encoded is None:
            return None
        decoded = self.decode_base64_authorization_header(encoded)
        if decoded is None:
            return None
        user, pwd = self.extract_user_credentials(decoded)
        if user is None or pwd is None:
            return None
        return self.user_object_from_credentials(user, pwd)
