from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.league import League
from models.team import Team


class Match(BaseModel, Model):
    __tablename__ = 'matches'
    __mapper_args__ = {'column_prefix': '_'}
    id = Column('id', Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League", back_populates="matches")
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    home_team = relationship("Team", back_populates="matches", primaryjoin="Team._id == Match._home_team_id")
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team = relationship("Team", back_populates="matches", primaryjoin="Team._id == Match._away_team_id")
    date = Column("date", DateTime())
    home_goals = Column("home_goals", Integer)
    away_goals = Column("away_goals", Integer)
    url = Column("url", String(255))
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    match_player_statistics = relationship("MatchPlayerStatistics")
    match_reports = relationship("MatchReport")
    match_statistics = relationship("MatchStatistics")

    def __init__(self, *args, league: League, home_team: Team, away_team: Team, **kwargs):
        super().__init__(*args)
        self._league = league
        self._home_team = home_team
        self._away_team = away_team
        self._home_goals = kwargs.get("home_goals", None)
        self._away_goals = kwargs.get("away_goals", None)
        self._date = kwargs.get("date", None)
        self._goals_home = kwargs.get("goals_home", 0)
        self._goals_away = kwargs.get("goals_away", 0)
        self._url = kwargs.get("url", "")
