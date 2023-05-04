#!/usr/bin/env python3
"""Session Class"""
import os
from api.v1.auth.auth import Auth
from models.user_session import UserSession

if os.getenv('AUTH_TYPE') == 'session':
    User = UserSession
else:
    User = None

    
class SessionAuth(Auth):
    """Class SessionAuth
    """
    pass
