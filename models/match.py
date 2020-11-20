from models.base_model import BaseModel
from models.league import League
from models.team import Team


class Match(BaseModel):
    def __init__(self, match_id, league: League, home_team: Team, away_team: Team):
        super().__init__(match_id)
        self._league = league
        self._home_team = home_team
        self._away_team = away_team
        self._date = None
        self._goals_home = 0
        self._goals_away = 0
        self._url = None
