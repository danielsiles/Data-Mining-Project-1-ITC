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

    def __init__(self, *args, team: Team, name, nationality, position):
        super().__init__(*args)
        self._team = team
        self._name = name
        self._nationality = nationality
        self._position = position
