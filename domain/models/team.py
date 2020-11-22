from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.league import League


class Team(BaseModel, Model):
    __tablename__ = 'teams'
    __mapper_args__ = {'column_prefix': '_'}
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League")
    table = relationship("LeagueTable")
    players = relationship("Player")
    matches = relationship("Match", primaryjoin="Team._id == Match._away_team_id")
    matche = relationship("Match", primaryjoin="Team._id == Match._home_team_id")
    url = Column('url', String(255))
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    match_player_statistics = relationship("MatchPlayerStatistics")
    match_reports = relationship("MatchReport")
    match_statistics = relationship("MatchStatistics")

    def __init__(self, *args, league: League, **kwargs):
        super().__init__(*args)
        self._league: League = league
        self._name = kwargs.get("name")
        self._url = kwargs.get("url")
