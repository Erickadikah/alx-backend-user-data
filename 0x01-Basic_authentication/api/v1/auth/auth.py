#!/usr/bin/env python3
"""Basic Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False:
            path and excluded_paths
            if path is None or excluded_paths is None
            or path not in excluded_paths and excluded_paths is None:
            return True
        else:
            if path is None:
                return True
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            return True
            if path.startswith(excluded_paths or path + '/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return : None
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Return: None
        """
        return None
