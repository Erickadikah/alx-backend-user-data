#!/usr/bin/env python3
"""BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Basic user Credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return decoded_base64_authorization_header.split(":")

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Basic User Object
            Args: user_email, user_pwd
            Return None if user_email is None or not a string
            Return None if user_pwd is None or not a string
            search of the User to lookup the list of users
        """
        if not isinstance(user_email, str) or None:
            return None
        if not isinstance(user_pwd, str) or None:
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if len(user) == 0:
            return None
        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user


    def current_user(self, request=None) -> TypeVar('User'):
        """Overload current_user"""
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        # Extract base64 authorization_header
        base64_header = self.extract_base64_authorization_header(authorization_header)
        if not base64_header:
            return None
        # decode
        decoded_header = self.decode_base64_authorization_header(base64_header)
        if not decoded_header:
            return None
        # Decoding base64 Auth
        user_credentials = self.extract_user_credentials(decoded_header)
        if not user_credentials:
            return None
        email, password = user_credentials[0], user_credentials[1]
        user = user_credentials[0], user_credentials[0]
        # Getting user object
        return self.user_object_from_credentials(user)