from domain.models.match_player_statistics import MatchPlayerStatistics
from infra.db.connection import db_session


class MatchPlayerStatisticsRepo:

    @staticmethod
    def create(match_player_statistics: MatchPlayerStatistics):
        db_session.merge(match_player_statistics)
        db_session.commit()
