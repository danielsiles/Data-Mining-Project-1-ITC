from abc import ABC, abstractmethod

from domain.models.match_report import MatchReport


class BaseMatchReportRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BaseMatchReportRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def create(self, match_report: MatchReport):
        pass
