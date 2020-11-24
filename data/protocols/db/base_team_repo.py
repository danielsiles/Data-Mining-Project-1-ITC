from abc import ABC

from domain.models.team import Team


class BaseTeamRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    def insert_or_update(self, team: Team):
        pass

    def find_by_name(self, league_id, name):
        pass


