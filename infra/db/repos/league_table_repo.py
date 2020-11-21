from infra.db.connection import db_session

class LeagueTableRepo:

    @staticmethod
    def update_league_table(league_table):
        db_session.merge(league_table)
        db_session.commit()
