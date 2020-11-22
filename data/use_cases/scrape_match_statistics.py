from sqlalchemy.exc import IntegrityError

from data.use_cases.base_use_case import BaseUseCase
from domain.models.match_statistics import MatchStatistics
from infra.db.connection import db_session
from infra.db.repos.match_repo import MatchRepo
from infra.db.repos.match_report_repo import MatchReportRepo
from infra.db.repos.match_statistics_repo import MatchStatisticsRepo
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match_report import MatchReport


class ScrapeMatchStatistics(BaseUseCase):

    def __init__(self, match_id, scraper: BaseScraper, parser: BaseParser):
        self.match_id = match_id
        self.scraper = scraper
        self.parser = parser

    def execute(self):
        match = MatchRepo.find_by_id(self.match_id)
        if match is None:
            raise ValueError("Match not found")
        try:
            html = self.scraper.scrape(match.get_url().replace("Show", "Live"))
        except Exception:
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        home_team, away_team = self.parser.parse(html)
        if home_team is None:
            raise ValueError("Could not parse HTML")

        self._insert_data(match, home_team)
        self._insert_data(match, away_team)

    def _insert_data(self, match, team_summary):
        try:
            team_summary["match_id"] = match.get_id()
            team_summary["team_id"] = match._home_team_id
            MatchStatisticsRepo.create(MatchStatistics(**team_summary))
        except IntegrityError:
            db_session.rollback()
            print("This match report already exists. Continuing...")