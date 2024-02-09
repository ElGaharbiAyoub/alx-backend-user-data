#!/usr/bin/env python3
""" loggoer """
from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ filter_datum """
    for field in fields:
        message = re.sub(
            "{}=.*?{}".format(field, separator),
            "{}={}{}".format(field, redaction, separator),
            message)
    return message
