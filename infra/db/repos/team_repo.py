from sqlalchemy import insert, inspect

from domain.models.team import Team
from infra.db.connection import db_session


class TeamRepo:

    @staticmethod
    def insert_or_update(team: Team):
        team = db_session.merge(team)
        db_session.commit()
        db_session.flush()
        db_session.refresh(team)
        return team

    @staticmethod
    def find_by_name(league_id, name):
        return db_session.query(Team).filter(Team.league_id == league_id).filter(Team.name == name).first()


