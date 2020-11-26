from abc import ABC, abstractmethod

from domain.models.match_player_statistics import MatchPlayerStatistics


class BaseMatchPlayerStatisticsRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    @abstractmethod
    def create(self, match_player_statistics: MatchPlayerStatistics):
        self._db_session.merge(match_player_statistics)
        self._db_session.commit()
