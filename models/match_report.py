from models.base_model import BaseModel
from models.league import League
from models.match import Match
from models.team import Team


class MatchReport(BaseModel):
    def __init__(self, match_report_id, match: Match, team: Team, report, type):
        super().__init__(match_report_id)
        self._match = match
        self._team = team
        self._report = report
        self._type = type
