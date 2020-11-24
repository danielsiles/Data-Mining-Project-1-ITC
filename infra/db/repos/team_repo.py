from data.protocols.db.base_team_repo import BaseTeamRepo
from domain.models.team import Team
from infra.db.connection import DBConnection


class TeamRepo(BaseTeamRepo):

    def __init__(self):
        super().__init__(DBConnection.get_db_session())

    def insert_or_update(self, team: Team):
        team = self._db_session.merge(team)
        self._db_session.commit()
        self._db_session.flush()
        self._db_session.refresh(team)
        return team

    def find_by_name(self, league_id, name):
        return self._db_session.query(Team).filter(Team.league_id == league_id).filter(Team.name == name).first()


