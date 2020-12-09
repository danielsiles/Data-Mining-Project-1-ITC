from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, UniqueConstraint, Float
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.league import League
from domain.models.team import Team


class MatchOdds(BaseModel, Model):
    __tablename__ = 'match_odds'
    __mapper_args__ = {'column_prefix': '_'}
    __table_args__ = (UniqueConstraint('match_id', 'site_name'),)

    id = Column('id', Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    match = relationship("Match", back_populates="match_odds")
    site_name = Column("site_name", String(255))
    home_win = Column("home_win", Float())
    draw = Column("draw", Float())
    home_loss = Column("home_loss", Float())
    last_update = Column('last_update', Integer())
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self._match_id = kwargs.get("match_id", None)
        self._match = kwargs.get("match", None)
        self._site_name = kwargs.get("site_name", None)
        self._home_win = kwargs.get("home_win", 0)
        self._draw = kwargs.get("draw", 0)
        self._home_loss = kwargs.get("home_loss", 0)
        self._last_update = kwargs.get("last_update", 0)

    def get_match_id(self):
        return self._match_id

    def get_id(self):
        return self._id

