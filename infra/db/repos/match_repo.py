from data.protocols.db.base_match_repo import BaseMatchRepo
from domain.models.match import Match
from infra.db.connection import DBConnection


class MatchRepo(BaseMatchRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def find_by_id(self, match_id):
        return self._db_session.query(Match).filter(Match.id == match_id).first()

    def insert_or_update(self, match):
        found_match = self._db_session.query(Match).filter(
            Match.home_team_id == match.get_home_team_id(),
            Match.away_team_id == match.get_away_team_id(),
            Match.date == match.get_date(),
        ).first()
        if found_match is None:
            self._db_session.add(match)
        else:
            self._db_session.query(Match).filter(
                Match.home_team_id == match.get_home_team_id(),
                Match.away_team_id == match.get_away_team_id(),
                Match.date == match.get_date(),
            ).update({Match.home_goals: match.get_home_goals(),
                      Match.away_goals: match.get_away_goals(),
                      Match.url: match.get_url()}, synchronize_session="fetch")

        self._db_session.commit()
