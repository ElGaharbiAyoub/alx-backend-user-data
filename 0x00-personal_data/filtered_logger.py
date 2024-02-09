#!/usr/bin/env python3
""" loggoer """
import re


def filter_datum(
        fields: list[str],
        redaction: str,
        message,
        separator: str) -> str:
    """ filter_datum """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
