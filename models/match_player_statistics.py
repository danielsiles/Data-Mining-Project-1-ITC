from models.base_model import BaseModel
from models.match import Match
from models.team import Team


class MatchPlayerStatistics(BaseModel):
    def __init__(self, match_player_statistics_id, match: Match, team: Team, player: Player):
        super().__init__(match_player_statistics_id)
        self._match = match
        self._team = team
        self._player = player
        self._shots = 0
        self._shots_on_target = 0
        self._key_passes = 0
        self._pass_success = 0
        self._aerials_won = 0
        self._touches = 0
        self._rating = 0
        self._dribbles_won = 0
        self._fouls_given = 0
        self._offside_given = 0
        self._dispossessed = 0
        self._turnover = 0
        self._tackles = 0
        self._interceptions = 0
        self._clearances = 0
        self._shots_blocked = 0
        self._fouls_committed = 0
        self._passes = 0
        self._crosses = 0
        self._cross_success = 0
        self._long_ball = 0
        self._long_ball_success = 0
        self._through_ball = 0
        self._through_ball_success = 0
