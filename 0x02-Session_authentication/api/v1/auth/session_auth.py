#!/usr/bin/env python3
"""Session Class"""
import os
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Class SessionAuth
    """
    def __init__(self):
        """initilaizer"""
        super().__init__()
