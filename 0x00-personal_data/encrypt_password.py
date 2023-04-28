#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash function for password encryption
        Args:
            password: str - The password to hash
        Returns:
            bytes - The salted, hashed password as a byte string
    """
    password = password.encode()
    salt: bytes = bcrypt.gensalt()
    encrypt_password: bytes = bcrypt.hashpw(password, salt)
    return encrypt_password


def is_valid(hash_password: bytes, password: str) -> bool:
    """Implementation to validate matched hashed
        password
        Implementation to validate matched hashed password
    Args:
        hashed_password: bytes - The hashed password to validate against
        password: str - The plain text password to validate
    Returns:
        bool - True if the password is valid, False otherwise
    """
    is_valid = False
    if bcrypt.checkpw(password.encode(), hash_password):
        is_valid = True
    return is_valid

