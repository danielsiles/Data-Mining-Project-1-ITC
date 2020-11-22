from infra.db.connection import db_session
from domain.models.match_report import MatchReport


class MatchReportRepo:

    def __init__(self, db_session):
        self.db_session = db_session

    @staticmethod
    def create(match_report: MatchReport):
        db_session.merge(match_report)
        db_session.commit()
