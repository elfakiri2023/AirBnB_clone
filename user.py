#!/usr/bin/python3
"""This is the User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """This is the User class"""
    
    first_name = ""
    last_name = ""
    password = ""
    email = ""

