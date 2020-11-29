from data.protocols.db.base_match_repo import BaseMatchRepo
from domain.models.league import League
from domain.models.match import Match
from infra.db.connection import DBConnection


class MatchRepo(BaseMatchRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def find_by_id(self, match_id):
        """
        Finds a match by id
        :param match_id: Id of the match
        :return: Match object if found or None
        """
        return self._db_session.query(Match).filter(Match.id == match_id).first()

    def insert_or_update(self, match):
        """
        Inserts a match into the database if not exists, otherwise update the existing one
        :param match: Match object containing the updated data
        """
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

    def get_matches(self, **kwargs):
        league = kwargs.get("league")
        date = kwargs.get("date")
        league = self._db_session.query(League).filter(League.name == league).first()
        if league is not False and date is not False:
            return self._db_session.query(Match)\
                .filter(Match.league_id == league.get_id() and Match.date > date).all()
        elif league is False and date is not False:
            return self._db_session.query(Match)\
                .filter(Match.date > date).all()
        else:
            return self._db_session.query(Match)\
                .filter(Match.date > date).all()
