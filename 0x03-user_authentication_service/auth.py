#!/usr/bin/env python3
""""Password hashing
"""
from bcrypt import hashpw, gensalt
import bcrypt
import base64
from db import DB, User
from typing import Union
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _generate_uuid() -> str:
    """This method returns a string representation of
        UUID
    """
    return str(uuid4())

# @staticmethod


def _hash_password(self, password: str) -> bytes:
    """Returns encrypted password
    Args: password
    """
    # salt = bcrypt.gensalt()
    # encoded_password = password.encode('utf-8')
    # hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """
    _db = DB()

    @staticmethod
    def valid_login(email: str, password: str) -> bool:
        """Valid login
        Args: email, Password
        """
        try:
            # finds user by email
            user = Auth._db.find_user_by(email=email)
        except NoResultFound:
            return False
            # checks if its a valid bcript password
        return bcrypt.checkpw(
            password.encode('utf-8'),
            user.hashed_password)

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """Getting user by session_id
            Args: session_id
            if there is no session_id :
            return None
            we find the user with session_id :
            return user
            else:
                return None
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy session
            Args: user_id
            find the user by user_id:
            then we udate the user using user.id,
            session to none
        """
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session=None)
            # return user
        except Exception:
            return None

    def register_user(self, email: str, password: str) -> User:
        """Create a new User by given Email and password
            if user exists with a given email return:
                User <user's email> already exists

        """
        # checking if user with email exists
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            # hashed the password

            hashed_password = _hash_password(self, password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

        # creating a new user and adding to the database.
        # user = User(email=email, hashed_password=hashed_password)
        # self._session.add(user)
        # self._session.commit()

    def create_session(self, email: str) -> str:
        """creating asession and creating uuid for each
        ARGS: email: str
        """
        try:
            # finding the user email
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return
