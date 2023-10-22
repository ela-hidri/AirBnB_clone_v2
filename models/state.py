#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False
                  )

    """cities = relationship('City',
                          backref='state',
                          cascade='all,delete-orphan',
                          uselist=True)
    """
    if getenv('HBNB__TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ get all """
            cities = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
