from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.league import League


class Team(BaseModel, Model):
    __tablename__ = 'teams'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League")
    table = relationship("LeagueTable")
    players = relationship("Player")
    matches = relationship("Match", primaryjoin="Team.id == Match.away_team_id")
    matche = relationship("Match", primaryjoin="Team.id == Match.home_team_id")
    url = Column('is_popular', String(255))

    match_player_statistics = relationship("MatchPlayerStatistics")
    match_reports = relationship("MatchReport")
    match_statistics = relationship("MatchStatistics")

    def __init__(self, team_id, league: League, **kwargs):
        super().__init__(team_id)
        self._league: League = league
        self._name = kwargs.get("name")
        self._url = kwargs.get("url")
