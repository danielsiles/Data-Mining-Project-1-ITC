from data.protocols.db.base_match_statistics_repo import BaseMatchStatisticsRepo
from domain.models.match_odds import MatchOdds
from infra.db.connection import DBConnection


class MatchOddsRepo(BaseMatchStatisticsRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def create(self, match_odds: MatchOdds):
        """
        Creates a new row of match statistics in the database
        :param match_odds: Match Odds object containing all the information
        """
        self._db_session.merge(match_odds)
        self._db_session.commit()
