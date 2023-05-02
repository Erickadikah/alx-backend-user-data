#!/usr/bin/env python3
"""BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth
    super().require_auth(path, excluded_paths)
    """
    pass
