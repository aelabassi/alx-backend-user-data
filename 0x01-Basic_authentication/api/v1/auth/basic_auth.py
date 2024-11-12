#!/usr/bin/env python3
""" Basic authentication module
"""
from api.v1.auth.auth import Auth
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
           type(base64_authorization_header) is not str:
            return None
        try:
            return base64_authorization_header.encode('utf-8').decode('base64')
        except Exception:
            return None
