from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from infra.db.connection import Model
from domain.models.base_model import BaseModel
from domain.models.match import Match
from domain.models.player import Player
from domain.models.team import Team


class MatchPlayerStatistics(BaseModel, Model):
    __tablename__ = 'match_player_statistics'
    __mapper_args__ = {'column_prefix': '_'}
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
    created_at = Column('created_at', DateTime())
    updated_at = Column('updated_at', DateTime())

    def __init__(self, *args, match: Match, team: Team, player: Player, **kwargs):
        super().__init__(*args)
        self._match = match
        self._team = team
        self._player = player
        self._match_id = kwargs.get("match_id")
        self._team_id = kwargs.get("team_id")
        self._player_id = kwargs.get("player_id")
        self._shots = kwargs.get("shots")
        self._shots_on_target = kwargs.get("shots_on_target")
        self._key_passes = kwargs.get("key_passes")
        self._pass_success = kwargs.get("pass_success")
        self._aerials_won = kwargs.get("aerials_won")
        self._touches = kwargs.get("touches")
        self._rating = kwargs.get("rating")
        self._dribbles_won = kwargs.get("dribbles_won")
        self._fouls_given = kwargs.get("fouls_given")
        self._offside_given = kwargs.get("offside_given")
        self._dispossessed = kwargs.get("dispossessed")
        self._turnover = kwargs.get("turnover")
        self._tackles = kwargs.get("tackles")
        self._interceptions = kwargs.get("interceptions")
        self._clearances = kwargs.get("clearances")
        self._shots_blocked = kwargs.get("shots_blocked")
        self._fouls_committed = kwargs.get("fouls_committed")
        self._passes = kwargs.get("passes")
        self._crosses = kwargs.get("crosses")
        self._cross_success = kwargs.get("cross_success")
        self._long_ball = kwargs.get("long_ball")
        self._long_ball_success = kwargs.get("long_ball_success")
        self._through_ball = kwargs.get("through_ball")
        self._through_ball_success = kwargs.get("through_ball_success")
