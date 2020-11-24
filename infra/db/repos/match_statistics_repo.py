from data.protocols.db.base_match_statistics_repo import BaseMatchStatisticsRepo
from domain.models.match_statistics import MatchStatistics
from infra.db.connection import DBConnection


class MatchStatisticsRepo(BaseMatchStatisticsRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def create(self, match_statistics: MatchStatistics):
        self._db_session.merge(match_statistics)
        self._db_session.commit()
