from data.protocols.db.base_league_repo import BaseLeagueRepo
from domain.models.league import League
from infra.db.connection import DBConnection


class LeagueRepo(BaseLeagueRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def find_by_name(self, league_name):
        """
        Finds a league by name
        :param league_name: Name of the league to search in database
        :return: League object of the found league or None
        """
        return self._db_session.query(League).filter(League.name == league_name).first()

    def get_all(self):
        """
        Get all leagues
        :return: List of all leagues
        """
        return self._db_session.query(League).all()
