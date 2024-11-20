#!/usr/bin/env python3
""" users model """
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    id: Column(Integer, primary_key=True)
    email: Column(String(128), nullable=False)
    hashed_password: Column(String(128), nullable=False)
    session_id: Column(String(128), nullable=True)
    reset_token: Column(String(128), nullable=True)
