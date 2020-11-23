from sqlalchemy import insert, inspect

from domain.models.player import Player
from domain.models.team import Team
from infra.db.connection import db_session


class PlayerRepo:

    @staticmethod
    def insert_or_update(player: Player):
        player = db_session.merge(player)
        db_session.commit()
        db_session.flush()
        db_session.refresh(player)
        return player

    @staticmethod
    def find_by_name(team_id, name):
        return db_session.query(Player).filter(Player.team_id == team_id).filter(Team.name == name).first()


