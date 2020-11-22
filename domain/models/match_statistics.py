from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.match import Match
from domain.models.team import Team


class MatchStatistics(BaseModel, Model):
    __tablename__ = 'match_statistics'
    __mapper_args__ = {'column_prefix': '_'}
    __table_args__ = (UniqueConstraint('match_id', 'team_id'),)
    id = Column('id', Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    match = relationship("Match", back_populates="match_statistics")
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="match_statistics")
    goals = Column("goals", Integer)
    ratings = Column("ratings", Integer)
    possession = Column("possession", Integer)
    pass_success = Column("pass_success", Integer)
    dribbles = Column("dribbles", Integer)
    aerials_won = Column("aerials_won", Integer)
    tackles = Column("tackles", Integer)
    corners = Column("corners", Integer)
    dispossessed = Column("dispossessed", Integer)
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self._match: Match = kwargs.get("match", 0)
        self._team: Team = kwargs.get("team", 0)
        self._match_id = kwargs.get("match_id", 0)
        self._team_id = kwargs.get("team_id", 0)
        self._goals = kwargs.get("goals", 0)
        self._ratings = kwargs.get("ratings", 0)
        self._possession = kwargs.get("possession", 0)
        self._pass_success = kwargs.get("pass_success", 0)
        self._dribbles = kwargs.get("dribbles", 0)
        self._aerials_won = kwargs.get("aerials_won", 0)
        self._tackles = kwargs.get("tackles", 0)
        self._corners = kwargs.get("corners", 0)
        self._dispossessed = kwargs.get("dispossessed", 0)
