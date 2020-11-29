from data.protocols.db.base_league_table_repo import BaseLeagueTableRepo
from infra.db.connection import DBConnection


class LeagueTableRepo(BaseLeagueTableRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def update_league_table(self, league_table):
        """
        Takes the league table object and updates the data in the database
        :param league_table: League Table object with updated data
        """
        self._db_session.merge(league_table)
        self._db_session.commit()
