#!/usr/bin/env python3
"""BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth


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
