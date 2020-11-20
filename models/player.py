from models.base_model import BaseModel
from models.team import Team


class Player(BaseModel):
    def __init__(self, player_id, team: Team, name, nationality, position):
        super().__init__(player_id)
        self._team = team
        self._name = name
        self._nationality = nationality
        self._position = position