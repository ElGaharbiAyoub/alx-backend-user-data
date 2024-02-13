#!/usr/bin/env python3
""" basic auth module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """BasicAuth class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extract base64 authorization header method
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]
