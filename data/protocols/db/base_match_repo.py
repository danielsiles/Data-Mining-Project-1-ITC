from abc import ABC

from domain.models.match import Match


class BaseMatchRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    def find_by_id(self, match_id):
        pass

    def insert_or_update(self, match):
        pass
