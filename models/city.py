#!/usr/bin/python3
"""
Module: city.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ the city class that inherits from BaseModel
    and stores the information of User's city """
    state_id = ''
    name = ''

    def __init__(self, state_id='', name='', *args, **kwargs):
        """ initializes the city class """
        super().__init__(*args, **kwargs)
        self.state_id = state_id
        self.name = str(name)
