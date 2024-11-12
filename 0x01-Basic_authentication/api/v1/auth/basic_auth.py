#!/usr/bin/env python3
""" Basic authentication module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


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
