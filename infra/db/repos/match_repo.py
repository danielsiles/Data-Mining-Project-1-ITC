from data.protocols.db.base_match_repo import BaseMatchRepo
from domain.models.match import Match
from infra.db.connection import DBConnection


class MatchRepo(BaseMatchRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def find_by_id(self, match_id):
        return self._db_session.query(Match).filter(Match.id == match_id).first()

    def insert_or_update(self, match):
        self._db_session.merge(match)
        self._db_session.commit()
