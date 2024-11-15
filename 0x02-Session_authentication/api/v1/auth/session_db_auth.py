#!/usr/bin/env python3
""" Session DB Auth
"""
from api.v1.auth.session_auth import SessionAuth
from uuid import uuid4


class SessionDBAuth(SessionAuth):
    """ Session DB Auth
    """
    def create_session(self, user_id=None):
        """Create a session ID"""
        if user_id is None:
            return None
        session_id = str(uuid4())
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return a User ID based on a Session ID"""
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None):
        """Destroy a session"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
