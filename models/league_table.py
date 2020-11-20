from models.base_model import BaseModel
from models.league import League
from models.team import Team


class LeagueTable(BaseModel):
    def __init__(self, league_table_id, league: League, team: Team, year):
        super().__init__(league_table_id)
        self._league = league
        self._team = team
        self._year = year
        self._matches_player = 0
        self._win = 0
        self._draw = 0
        self._loss = 0
        self._goal_for = 0
        self._goal_against = 0
        self._goal_difference = 0
        self._points = 0
