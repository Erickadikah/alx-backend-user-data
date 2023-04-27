#!/usr/bin/env python3
"""filter_datum that returns the log message obfuscated
"""
import logging
import re

from attr import fields


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        """
        pass


def filter_datum(fields, redaction, message, separator):
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character
    is separating all fields in the log line (message)
    """
    # define regex pattern to match field name and value
    pattern = r"([^=;]+)=([^;]+)"

    # split message into individual fields using the separator
    log_fields = re.findall(pattern, message)

    # obfuscate the specified fields
    for i, (field_name, field_value) in enumerate(log_fields):
        if field_name in fields:
            log_fields[i] = (field_name, redaction)
        elif re.match(r'\d{2}/\d{2}/\d{4}', field_value):
            log_fields[i] = (field_name, redaction)

    # join the obfuscated fields back into a log message using separator
    obfuscated_fields = ["{}={}".format(k, v) for k, v in log_fields]
    obfuscated_message = separator.join(obfuscated_fields)

    # return the obfuscated log message
    return obfuscated_message
