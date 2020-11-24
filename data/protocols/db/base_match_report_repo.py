from abc import ABC

from domain.models.match_report import MatchReport


class BaseMatchReportRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    def create(self, match_report: MatchReport):
        pass