from data.protocols.db.base_league_repo import BaseLeagueRepo
from domain.models.league import League
from infra.db.connection import DBConnection


class LeagueRepo(BaseLeagueRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def find_by_name(self, league_name):
        return self._db_session.query(League).filter(League.name == league_name).first()
