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
