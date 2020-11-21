from infra.db.connection import db_session


class MatchRepo:

    @staticmethod
    def insert_or_update_match(match):
        db_session.merge(match)
