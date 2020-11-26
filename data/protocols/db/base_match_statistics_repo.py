from abc import ABC, abstractmethod

from domain.models.match_statistics import MatchStatistics


class BaseMatchStatisticsRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    @abstractmethod
    def create(self, match_statistics: MatchStatistics):
        pass
