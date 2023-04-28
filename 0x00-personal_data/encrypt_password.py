#!/usr/bin/env python3
"""Encrypting passwords"""

from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    """Hash function for password encryption
        Args:
            password: str - The password to hash
        Returns:
            bytes - The salted, hashed password as a byte string
    """
    password = password.encode()
    salt: bytes = gensalt()
    encrypt_password: bytes = hashpw(password, salt)
    return encrypt_password
