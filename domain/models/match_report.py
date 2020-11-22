from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.match import Match
from domain.models.team import Team


class MatchReport(BaseModel, Model):
    __tablename__ = 'match_reports'
    __mapper_args__ = {'column_prefix': '_'}
    __table_args__ = (UniqueConstraint('match_id', 'team_id', 'report'),)

    id = Column('id', Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    match = relationship("Match", back_populates="match_reports")
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="match_reports")
    report = Column("report", String(255))
    type = Column("type", String(255))
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    def __init__(self, *args, match: Match, team: Team, **kwargs):
        super().__init__(*args)
        self._match = match
        self._team = team
        self._match_id = kwargs.get("match_id", 0)
        self._team_id = kwargs.get("team_id", 0)
        self._report = kwargs.get("report", "")
        self._type = kwargs.get("type", "")
