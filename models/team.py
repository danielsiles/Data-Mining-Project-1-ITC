from models.base_model import BaseModel
from models.league import League


class Team(BaseModel):
    def __init__(self, team_id, name, league: League, url):
        super().__init__(team_id)
        self._league: League = league
        self._name = name
        self._url = url
