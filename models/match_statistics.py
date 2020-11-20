from models.base_model import BaseModel
from models.match import Match
from models.team import Team


class MatchStatistics(BaseModel):
    def __init__(self, match_statistics_id, match: Match, team: Team):
        super().__init__(match_statistics_id)
        self._match = match
        self._team = team
        self._goals = 0
        self._ratings = 0
        self._possession = 0
        self._pass_success = 0
        self._dribbles = 0
        self._aerials_won = 0
        self._tackles = 0
        self._corners = 0
        self._dispossessed = 0
