from data.protocols.db.base_player_repo import BasePlayerRepo
from domain.models.team import Team
from domain.models.player import Player
from infra.db.connection import DBConnection


class PlayerRepo(BasePlayerRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def insert_or_update(self, player: Player):
        player = self._db_session.merge(player)
        self._db_session.commit()
        self._db_session.flush()
        self._db_session.refresh(player)
        return player

    def find_by_name(self, team_id, name):
        return self._db_session.query(Player).filter(Player.team_id == team_id).filter(Team.name == name).first()
