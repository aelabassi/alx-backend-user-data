#!/usr/bin/env python3
""" Regex-ing """
import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated
    Args:
        fields (List[str]): a list of strings representing
         all fields to obfuscate
        redaction (str): a string representing by what the
         field will be obfuscated
        message (str): a string representing the log line
        separator (str): a string representing by which
         character is separating all fields
         Returns:
            str: the log message obfuscated
             """
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format
        """
        return filter_datum(self.__fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
