from models.base_model import BaseModel


class League(BaseModel):
    def __init__(self, league_id, name, url):
        super().__init__(league_id)
        self._name = name
        self._url = url
        self._is_popular = True
