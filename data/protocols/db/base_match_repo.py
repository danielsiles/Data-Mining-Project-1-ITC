from abc import ABC, abstractmethod


class BaseMatchRepo(ABC):

    def __init__(self, db_session):
        """
        Constructor of BaseMatchRepo class
        :param db_session: Database session
        """
        self._db_session = db_session

    @abstractmethod
    def find_by_id(self, match_id):
        pass

    @abstractmethod
    def get_recent_matches(self, team_id):
        pass

    @abstractmethod
    def get_most_recent_match(self, home_team_name, away_team_name):
        pass

    @abstractmethod
    def insert_or_update(self, match):
        pass
