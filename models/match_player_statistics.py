from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from models.base_model import BaseModel
from models.match import Match
from models.player import Player
from models.team import Team


class MatchPlayerStatistics(BaseModel, Model):
    __tablename__ = 'match_player_statistics'
    id = Column('id', Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    match = relationship("Match", back_populates="match_player_statistics")
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="match_player_statistics")
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="match_player_statistics")
    shots = Column("shots", Integer)
    shots_on_target = Column("shots_on_target", Integer)
    key_passes = Column("key_passes", Integer)
    pass_success = Column("pass_success", Integer)
    aerials_won = Column("aerials_won", Integer)
    touches = Column("touches", Integer)
    rating = Column("rating", Integer)
    dribbles_won = Column("dribbles_won", Integer)
    fouls_given = Column("fouls_given", Integer)
    offside_given = Column("offside_given", Integer)
    dispossessed = Column("dispossessed", Integer)
    turnover = Column("turnover", Integer)
    tackles = Column("tackles", Integer)
    interceptions = Column("interceptions", Integer)
    clearances = Column("clearances", Integer)
    shots_blocked = Column("shots_blocked", Integer)
    fouls_committed = Column("fouls_committed", Integer)
    passes = Column("passes", Integer)
    crosses = Column("crosses", Integer)
    cross_success = Column("cross_success", Integer)
    long_ball = Column("long_ball", Integer)
    long_ball_success = Column("long_ball_success", Integer)
    through_ball = Column("through_ball", Integer)
    through_ball_success = Column("through_ball_success", Integer)

    def __init__(self, match_player_statistics_id, match: Match, team: Team, player: Player, **kwargs):
        super().__init__(match_player_statistics_id)
        self._match = match
        self._team = team
        self._player = player
        self._shots = kwargs.get("shots", 0)
        self._shots_on_target = kwargs.get("shots_on_target", 0)
        self._key_passes = kwargs.get("key_passes", 0)
        self._pass_success = kwargs.get("pass_success", 0)
        self._aerials_won = kwargs.get("aerials_won", 0)
        self._touches = kwargs.get("touches", 0)
        self._rating = kwargs.get("rating", 0)
        self._dribbles_won = kwargs.get("dribbles_won", 0)
        self._fouls_given = kwargs.get("fouls_given", 0)
        self._offside_given = kwargs.get("offside_given", 0)
        self._dispossessed = kwargs.get("dispossessed", 0)
        self._turnover = kwargs.get("turnover", 0)
        self._tackles = kwargs.get("tackles", 0)
        self._interceptions = kwargs.get("interceptions", 0)
        self._clearances = kwargs.get("clearances", 0)
        self._shots_blocked = kwargs.get("shots_blocked", 0)
        self._fouls_committed = kwargs.get("fouls_committed", 0)
        self._passes = kwargs.get("passes", 0)
        self._crosses = kwargs.get("crosses", 0)
        self._cross_success = kwargs.get("cross_success", 0)
        self._long_ball = kwargs.get("long_ball", 0)
        self._long_ball_success = kwargs.get("long_ball_success", 0)
        self._through_ball = kwargs.get("through_ball", 0)
        self._through_ball_success = kwargs.get("through_ball_success", 0)
