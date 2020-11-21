from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.league import League
from models.team import Team


class Match(BaseModel, Model):
    __tablename__ = 'matches'
    id = Column('id', Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League", back_populates="matches")
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    home_team = relationship("Team", back_populates="matches")
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team = relationship("Team", back_populates="matches")
    date = Column("date", DateTime())
    goals_home = Column("goals_home", Integer)
    goals_away = Column("goals_away", Integer)
    url = Column("url", String(255))

    def __init__(self, match_id, league: League, home_team: Team, away_team: Team, **kwargs):
        super().__init__(match_id)
        self._league = league
        self._home_team = home_team
        self._away_team = away_team
        self._date = kwargs.get("date", None)
        self._goals_home = kwargs.get("goals_home", 0)
        self._goals_away = kwargs.get("goals_away", 0)
        self._url = kwargs.get("url", "")
