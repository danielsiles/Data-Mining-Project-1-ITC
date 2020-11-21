from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.league import League
from models.match import Match
from models.team import Team


class MatchReport(BaseModel, Model):
    __tablename__ = 'match_reports'
    __mapper_args__ = {'column_prefix': '_'}
    id = Column('id', Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    match = relationship("Match", back_populates="match_reports")
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="match_reports")
    report = Column("report", String(255))
    type = Column("type", String(255))

    def __init__(self, *args, match: Match, team: Team, report, report_type):
        super().__init__(*args)
        self._match = match
        self._team = team
        self._report = report
        self._type = report_type
