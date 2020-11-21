import datetime

from sqlalchemy import Integer, Column, String, Boolean

from infra.db.connection import Model
from models.base_model import BaseModel


class League(BaseModel, Model):
    __tablename__ = 'leagues'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    url = Column('url', String(200))
    is_popular = Column('is_popular', Boolean())

    def __init__(self, league_id, **kwargs):
        super().__init__(league_id)
        self._name = kwargs.get("name")
        self._url = kwargs.get("url")
        self._is_popular = kwargs.get("is_popular")
