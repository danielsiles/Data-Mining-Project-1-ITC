import datetime

from sqlalchemy import Integer, Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel


class League(BaseModel, Model):
    __tablename__ = 'leagues'
    __mapper_args__ = {'column_prefix': '_'}
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    url = Column('url', String(200))
    is_popular = Column('is_popular', Boolean())
    teams = relationship("Team", back_populates="league")
    table = relationship("LeagueTable", back_populates="league")
    matches = relationship("Match", back_populates="league")
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self._name = kwargs.get("name")
        self._url = kwargs.get("url")
        self._is_popular = kwargs.get("is_popular")

    def __str__(self):
        return str(self.__dict__)
