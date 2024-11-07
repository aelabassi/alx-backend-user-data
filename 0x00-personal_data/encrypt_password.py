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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validate password
    Args:
        hashed_password (bytes): encrypted password
        password (str): string to validate
    Returns:
        bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
