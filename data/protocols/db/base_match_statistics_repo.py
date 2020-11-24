from abc import ABC

from domain.models.match_statistics import MatchStatistics


class BaseMatchStatisticsRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    def create(self, match_statistics: MatchStatistics):
        pass
