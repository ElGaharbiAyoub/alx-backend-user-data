#!/usr/bin/env python3
""" basic auth module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """BasicAuth class
    """
