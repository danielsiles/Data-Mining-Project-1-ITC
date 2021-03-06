from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.league import League
from domain.models.team import Team


class LeagueTable(BaseModel, Model):
    __tablename__ = 'tables'
    __mapper_args__ = {'column_prefix': '_'}
    __table_args__ = (UniqueConstraint('league_id', 'team_id', 'year'),)

    # id = Column('id', Integer, autoincrement=True)
    league_id = Column(Integer, ForeignKey('leagues.id'), primary_key=True, autoincrement=False)
    league = relationship("League", back_populates="table")
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True, autoincrement=False)
    team = relationship("Team", back_populates="table")
    year = Column("year", String(100))
    matches_played = Column("matches_played", Integer)
    win = Column("win", Integer)
    draw = Column("draw", Integer)
    loss = Column("loss", Integer)
    goal_for = Column("goal_for", Integer)
    goal_against = Column("goal_against", Integer)
    goal_difference = Column("goal_difference", Integer)
    points = Column("points", Integer)
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    def __init__(self, *args, league: League, team: Team, year, **kwargs):
        super().__init__(*args)
        self._league = league
        self._team = team
        self._year = year
        self._league_id = kwargs.get("league_id", 0)
        self._team_id = kwargs.get("team_id", 0)
        self._matches_played = kwargs.get("matches_played", 0)
        self._win = kwargs.get("win", 0)
        self._draw = kwargs.get("draw", 0)
        self._loss = kwargs.get("loss", 0)
        self._goal_for = kwargs.get("goal_for", 0)
        self._goal_against = kwargs.get("goal_against", 0)
        self._goal_difference = kwargs.get("goal_difference", 0)
        self._points = kwargs.get("points", 0)
