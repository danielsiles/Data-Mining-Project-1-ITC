from data.protocols.db.base_match_player_statistics_repo import BaseMatchPlayerStatisticsRepo
from domain.models.match_player_statistics import MatchPlayerStatistics
from infra.db.connection import DBConnection


class MatchPlayerStatisticsRepo(BaseMatchPlayerStatisticsRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def create(self, match_player_statistics: MatchPlayerStatistics):
        """
        Creates a new row of player statistics in the database
        :param match_player_statistics: Match player statistics object containing all the information
        """
        self._db_session.merge(match_player_statistics)
        self._db_session.commit()
