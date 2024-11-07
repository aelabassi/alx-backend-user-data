#!/usr/bin/env python3
""" Regex-ing """
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
