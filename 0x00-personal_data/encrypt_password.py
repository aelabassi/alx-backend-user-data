#!/usr/bin/env python3
""" Encrypt password """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Encrypt password
    Args:
        password (str): string to encrypt
    Returns:
        bytes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
