from abc import ABC, abstractmethod

from domain.models.team import Team


class BaseTeamRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    @abstractmethod
    def insert_or_update(self, team: Team):
        pass

    @abstractmethod
    def find_by_name(self, league_id, name):
        pass


