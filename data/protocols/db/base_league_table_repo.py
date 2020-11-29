from abc import ABC, abstractmethod


class BaseLeagueTableRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BaseLeagueTableRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def update_league_table(self, league_table):
        pass
