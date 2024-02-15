#!/usr/bin/env python3
""" session exp auth module
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta
from typing import TypeVar
import uuid


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class
    """
    def __init__(self):
        """Constructor
        """
        self.session_duration = int(getenv('SESSION_DURATION', 0))

    def create_session(self, user_id: str = None) -> str:
        """Create session method
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(
            self,
            session_id: str = None) -> str:
        """User id for session id method
        """
        if session_id is None or type(session_id) is not str:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get("user_id")
        if "created_at" not in session_dictionary:
            return None
        if (datetime.now() - session_dictionary.get("created_at")
                > timedelta(seconds=self.session_duration)):
            return None
        return session_dictionary.get("user_id")
