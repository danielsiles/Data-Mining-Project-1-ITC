from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.league import League
from models.team import Team


class LeagueTable(BaseModel, Model):
    __tablename__ = 'tables'
    id = Column('id', Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League", back_populates="tables")
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="tables")
    year = Column("year", String(100))
    matches_played = Column("matches_played", Integer)
    win = Column("win", Integer)
    draw = Column("draw", Integer)
    loss = Column("loss", Integer)
    goal_for = Column("goal_for", Integer)
    goal_against = Column("goal_against", Integer)
    goal_difference = Column("goal_difference", Integer)
    points = Column("points", Integer)

    def __init__(self, league_table_id, league: League, team: Team, year, **kwargs):
        super().__init__(league_table_id)
        self._league = league
        self._team = team
        self._year = year
        self._matches_played = kwargs.get("matches_played", 0)
        self._win = kwargs.get("win", 0)
        self._draw = kwargs.get("draw", 0)
        self._loss = kwargs.get("loss", 0)
        self._goal_for = kwargs.get("goal_for", 0)
        self._goal_against = kwargs.get("goal_against", 0)
        self._goal_difference = kwargs.get("goal_difference", 0)
        self._points = kwargs.get("points", 0)
