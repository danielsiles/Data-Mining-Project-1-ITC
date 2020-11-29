from abc import ABC, abstractmethod


class BaseLeagueRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BaseLeagueRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def find_by_name(self, league_name):
        pass
