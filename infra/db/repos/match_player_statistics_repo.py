from data.protocols.db.base_match_player_statistics_repo import BaseMatchPlayerStatisticsRepo
from domain.models.match_player_statistics import MatchPlayerStatistics
from infra.db.connection import DBConnection


class MatchPlayerStatisticsRepo(BaseMatchPlayerStatisticsRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def create(self, match_player_statistics: MatchPlayerStatistics):
        self._db_session.merge(match_player_statistics)
        self._db_session.commit()
