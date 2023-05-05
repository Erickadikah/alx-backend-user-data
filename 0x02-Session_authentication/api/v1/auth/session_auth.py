#!/usr/bin/env python3
"""Session Class"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Class SessionAuth
    """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """Creatign a session Id for user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id


    def user_id_for_session_id(self, session_id: str = None) -> str:
        """isntance of class session
            Return: user ID on Session ID
        """
        if session_id is None:
            return None
        if  not  isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id