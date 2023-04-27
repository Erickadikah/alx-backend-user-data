#!/usr/bin/env python3
"""filter_datum that returns the log message obfuscated
"""
import logging
import re
from typing import List


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
