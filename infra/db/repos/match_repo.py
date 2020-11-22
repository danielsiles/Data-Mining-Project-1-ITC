from infra.db.connection import db_session
from domain.models.match import Match


class MatchRepo:

    @staticmethod
    def find_by_id(match_id):
        return db_session.query(Match).filter(Match.id == match_id).first()

    @staticmethod
    def insert_or_update(match):
        db_session.merge(match)
        db_session.commit()
