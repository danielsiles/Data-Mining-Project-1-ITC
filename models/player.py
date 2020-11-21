from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.team import Team


class Player(BaseModel, Model):
    __tablename__ = 'players'
    id = Column('id', Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="players")
    name = Column("name", String(255))
    nationality = Column("nationality", String(255))
    position = Column("position", String(255))
    match_player_statistics = relationship("MatchPlayerStatistics")

    def __init__(self, player_id, team: Team, name, nationality, position):
        super().__init__(player_id)
        self._team = team
        self._name = name
        self._nationality = nationality
        self._position = position
