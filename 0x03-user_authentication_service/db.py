#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User
from user import Base
from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Creating add_user method
            Args: user_email, user_password
            return: User_id
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
            by email and password
            Retrieve a user by their email address.

         Args:
            email (str): Email address of the user to retrieve.
            session (Session): SQLAlchemy session to use for the query.

        Returns:
            User: The retrieved user object.
        Kwargs: email, hashed_password
        """
        if not kwargs:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updating User by id
            raises ValueError:
            to atleast one Field must be provided for update
        Args: user_id, kwargs
        """
        try:
            user = self._session.query(User).get(user_id)
            if user is None:
                raise NoResultFound
            for key, value in kwargs.items():
                setattr(user, key, value)
            self._session.commit()
            return user
        except NoResultFound:
            raise ValueError
