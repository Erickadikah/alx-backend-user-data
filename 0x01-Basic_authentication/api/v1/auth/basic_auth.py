#!/usr/bin/env python3
"""BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """class BasicAuth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Args: authorization_header
            this function
            Return None if authorization_header is None
            Return None if authorization_header is not
            a string
            Return None if authorization_header doesn’t
            start by Basic
                : Otherwise, return the value after Basic
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None
