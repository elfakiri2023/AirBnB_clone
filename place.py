#!/usr/bin/python3
"""This is the Place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """This is the Place class"""
   
    amenity_ids = []
    description = ""
    price_by_night = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    longitude = 0.0
    latitude = 0.0
    user_id = ""
    city_id = ""
    name = ""

