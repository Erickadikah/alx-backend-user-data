#!/usr/bin/env python3
"""filter_datum that returns the log message obfuscated
"""
import re
import logging
from typing import List
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """to be filled
        """
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.msg,
            self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """this function returns a logging.Logger
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """This function returns a connection
        to The database
        Args: None
        Obtain MySQL credentials from environment variables
    mysdb = mysql.connector.connect(
        PERSONAL_DATA_DB_HOST = 'localhost',
        PERSONAL_DATA_DB_USERNAME = 'root',
        PERSONAL_DATA_DB_PASSWORD = '',
        db = 'PERSONAL_DATA_DB_NAME
    Return: -> mysql.connector.connection.MySQLConnection
    """
    mydb_connection = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return mydb_connection


def main() -> None:
    """Reading and filtering data
        Args: None
        Function: Obtains database connection using get_db
        Retieves all row in the users Table
        Returns each row
        logger: logging.Logger = get_logger()
        get a logger object and assigns it to a variable logger
    """
    logger: logging.logger = get_logger()
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users;')
    fields = ['name', 'email', 'phone', 'ssn',
              'password', 'ip', 'last_login', 'user_agent']
    filtered_fields = ['name', 'email', 'phone', 'ssn', 'password']
    results = cursor.fetchall()
    for row in results:
        data = dict(zip(fields, row))
        filtered_data = {key: '***' if key in filtered_fields else values
                         for key, values in data.items()}
        credentials = "name={name}; email={email};\
        phone={phone}; ssn={ssn}; password={password};\
              ip={ip}; last_login={last_login}; user_agent={user_agent};"
        logger.info(credentials.format(**filtered_data))
        logger.info('Filtered fields: %s', ', '.join(filtered_fields))
    cursor.close()
    connection.close()


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character
    is separating all fields in the log line (message)
    return: re.sub
    """
    return re.sub('|'.join(f'(?<={field}=).*?(?={separator})'
                           for field in fields), redaction, message)


if __name__ == '__main__':
    main()
