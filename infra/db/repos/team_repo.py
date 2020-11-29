from data.protocols.db.base_team_repo import BaseTeamRepo
from domain.models.team import Team
from infra.db.connection import DBConnection


class TeamRepo(BaseTeamRepo):

    def __init__(self):
        """
        Constructor of LeagueRepo. Initializes the instance with the database session.
        """
        super().__init__(DBConnection.get_db_session())

    def insert_or_update(self, team: Team):
        """
        Inserts a team into the database if not exists, otherwise update the existing one
        :param team: Team object containing the updated data
        """
        team = self._db_session.merge(team)
        self._db_session.commit()
        self._db_session.flush()
        self._db_session.refresh(team)
        return team

    def find_by_name(self, league_id, name):
        """
        Finds a team by league_id and name
        :param league_id: Id of the league
        :param name: Name of the team
        :return: Team object if found or None
        """
        return self._db_session.query(Team).filter(Team.league_id == league_id).filter(Team.name == name).first()


