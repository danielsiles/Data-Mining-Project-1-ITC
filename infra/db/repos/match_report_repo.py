from infra.db.connection import db_session
from models.match_report import MatchReport


class MatchReportRepo:

    @staticmethod
    def create(match_report: MatchReport):
        db_session.merge(match_report)
        db_session.commit()
