from abc import ABC, abstractmethod

from domain.models.league import League


class BaseLeagueRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    @abstractmethod
    def find_by_name(self, league_name):
        pass