from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.team import Team


class Player(BaseModel, Model):
    __tablename__ = 'players'
    __mapper_args__ = {'column_prefix': '_'}
    id = Column('id', Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="players")
    name = Column("name", String(255))
    nationality = Column("nationality", String(255))
    position = Column("position", String(255))
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    match_player_statistics = relationship("MatchPlayerStatistics")

    def __init__(self, *args, team: Team, **kwargs):
        super().__init__(*args)
        self._team = team
        self._team_id = kwargs.get("team_id")
        self._name = kwargs.get("name")
        self._nationality = kwargs.get("nationality")
        self._position = kwargs.get("position")

    def get_id(self):
        return self._id