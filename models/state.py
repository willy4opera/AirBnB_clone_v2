#!/usr/bin/python3

"""The state class"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """The class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        dev_var = models.storage.all()
        dev_lst = []
        solution = []
        for key in dev_var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                dev_lst.append(dev_var[key])
        for elem in dev_lst:
            if (elem.state_id == self.id):
                solution.append(elem)
        return (solution)
