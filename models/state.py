#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City
from models import storage_type
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instance
            with state_id == State.id
            """
            found = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    found.append(city)
            return found
