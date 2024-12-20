#!/usr/bin/env python3
""" Session expiration """
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime
from os import getenv


class SessionExpAuth(SessionAuth):
    """ Session expiration """
    def __init__(self):
        SESSION_DURATION = getenv("SESSION_DURATION")
        try:
            session_duration = int(SESSION_DURATION)
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id: str = None) -> str:
        """ Create a session ID """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return a User ID based on a Session ID """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get("user_id")
        if "created_at" not in session_dictionary:
            return None
        created_at = session_dictionary.get("created_at")
        if created_at is None:
            return None
        if (datetime.now() - created_at).seconds > self.session_duration:
            return None
        return session_dictionary.get("user_id")
