from abc import ABC, abstractmethod

from domain.models.match import Match


class BaseMatchRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BaseMatchRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def find_by_id(self, match_id):
        pass

    @abstractmethod
    def insert_or_update(self, match):
        pass
