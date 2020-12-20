from sqlalchemy import or_
from sqlalchemy.orm import aliased

from data.protocols.db.base_match_repo import BaseMatchRepo
from domain.models.league import League
from domain.models.match import Match
from domain.models.team import Team
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

    def get_recent_matches(self, team_id):
        return self._db_session.query(Match).filter(or_(
            Match.home_team_id == team_id,
            Match.away_team_id == team_id)).all()

    def get_most_recent_match(self, home_team_name, away_team_name):
        home_team = aliased(Team, name="teams_1")
        away_team = aliased(Team, name="teams_2")
        return self._db_session.execute(
            f"SELECT matches.id AS matches_id, matches.league_id AS matches_league_id,matches.home_team_id "
            f"AS matches_home_team_id, matches.away_team_id AS matches_away_team_id,matches.date AS matches_date,"
            f" matches.home_goals AS matches_home_goals, matches.away_goals AS matches_away_goals, matches.url"
            f" AS matches_url,matches.created_at AS matches_created_at, matches.updated_at AS matches_updated_at"
            f" FROM matches INNER JOIN teams AS teams_1 ON teams_1.id = matches.home_team_id INNER JOIN "
            f"teams AS teams_2 ON teams_2.id = matches.away_team_id WHERE teams_1.name = \'{home_team_name}\'"
            f" OR teams_2.name = \'{away_team_name}\' LIMIT 1").first()

    def get_matches(self, **kwargs):
        league = kwargs.get("league")
        date = kwargs.get("date")
        league = self._db_session.query(League).filter(League.name == league).first()
        if league is not False and date is not False:
            return self._db_session.query(Match) \
                .filter(Match.league_id == league.get_id() and Match.date > date).all()
        elif league is False and date is not False:
            return self._db_session.query(Match) \
                .filter(Match.date > date).all()
        else:
            return self._db_session.query(Match).all()
