from infra.db.connection import db_session
from models.league import League


class LeagueRepo:

    @staticmethod
    def find_by_name(league_name):
        return db_session.query(League).filter(League.name == league_name).first()
