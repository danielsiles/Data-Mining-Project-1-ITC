from data.protocols.db.base_match_report_repo import BaseMatchReportRepo
from domain.models.match_report import MatchReport
from infra.db.connection import DBConnection


class MatchReportRepo(BaseMatchReportRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def create(self, match_report: MatchReport):
        self._db_session.merge(match_report)
        self._db_session.commit()
