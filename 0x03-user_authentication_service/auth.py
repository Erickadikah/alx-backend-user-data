#!/usr/bin/env python3
""""Password hashing
"""
from bcrypt import hashpw, gensalt
import bcrypt
import base64
from db import DB, User
from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _generate_uuid() -> str:
    """This method returns a string representation of
        UUID
    """
    return str(uuid4())



class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()


    @staticmethod
    def _hash_password(self, password: str) -> bytes:
        """Returns encrypted password
        Args: password
        """
        # salt = bcrypt.gensalt()
        # encoded_password = password.encode('utf-8')
        # hashed_password = bcrypt.hashpw(encoded_password, salt)
        return hashpw(password.encode('utf-8'), gensalt())

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

            hashed_password = Auth._hash_password(self, password)
            new_user = self._db.add_user(email, hashed_password)

        # creating a new user and adding to the database.
        # user = User(email=email, hashed_password=hashed_password)
        # self._session.add(user)
        # self._session.commit()
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Valid login
        Args: email, Password
        """
        try:
            # finds user by email
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
                # checks if its a valid bcript password
        return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password)
            # else:
                # return False

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
