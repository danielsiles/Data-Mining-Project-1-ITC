from abc import ABC, abstractmethod

from domain.models.player import Player


class BasePlayerRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BasePlayerRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def insert_or_update(self, player: Player):
        pass

    @abstractmethod
    def find_by_name(self, team_id, name):
        pass
