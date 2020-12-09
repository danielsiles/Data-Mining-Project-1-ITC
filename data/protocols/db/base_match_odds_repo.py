from abc import ABC, abstractmethod

from domain.models.match_odds import MatchOdds


class BaseMatchOddsRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BaseMatchOddsRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def create(self, match_odds: MatchOdds):
        pass
