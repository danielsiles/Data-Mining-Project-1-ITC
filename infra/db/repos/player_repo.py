from data.protocols.db.base_player_repo import BasePlayerRepo
from domain.models.player import Player
from infra.db.connection import DBConnection


class PlayerRepo(BasePlayerRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def insert_or_update(self, player: Player):
        """
        Inserts a player into the database if not exists, otherwise update the existing one
        :param player: Player object containing the updated data
        """
        player = self._db_session.merge(player)
        self._db_session.commit()
        self._db_session.flush()
        self._db_session.refresh(player)
        return player

    def find_by_name(self, team_id, name):
        """
        Finds a player by name and team_id
        :param team_id: Id of the team
        :param name: Name of the player
        :return: Player object if found or None
        """
        return self._db_session.query(Player).filter(Player.team_id == team_id).filter(Player.name == name).first()
