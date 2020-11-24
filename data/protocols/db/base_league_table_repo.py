from abc import ABC


class BaseLeagueTableRepo(ABC):

    def __init__(self, db_session):
        self._db_session = db_session

    def update_league_table(self, league_table):
        pass
