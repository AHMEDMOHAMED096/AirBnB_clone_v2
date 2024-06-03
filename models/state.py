#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    # Getter in case of storage type is FileStorage
    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            from models import storage

            """ getter method that returns list of City instances """
            return [
                City
                for _, City in storage.all("City").items()
                if City.state_id == self.id
            ]
