from data.protocols.db.base_match_report_repo import BaseMatchReportRepo
from domain.models.match_report import MatchReport
from infra.db.connection import DBConnection


class MatchReportRepo(BaseMatchReportRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def create(self, match_report: MatchReport):
        """
        Creates a new row of match report in the database
        :param match_report: Match report object containing all the information
        """
        self._db_session.merge(match_report)
        self._db_session.commit()
