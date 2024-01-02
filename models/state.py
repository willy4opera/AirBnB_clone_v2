#!/usr/bin/python3

"""Here, we defines the state class"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        d_var = models.storage.all()
        dev_list = []
        product = []
        for key in d_var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                dev_list.append(d_var[key])
        for elem in dev_list:
            if (elem.state_id == self.id):
                product.append(elem)
        return (product)
