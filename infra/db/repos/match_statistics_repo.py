from infra.db.connection import db_session
from domain.models.match_statistics import MatchStatistics


class MatchStatisticsRepo:

    @staticmethod
    def create(match_statistics: MatchStatistics):
        db_session.merge(match_statistics)
        db_session.commit()
