from sqlalchemy.exc import IntegrityError

from data.use_cases.base_use_case import BaseUseCase
from infra.db.connection import db_session
from infra.db.repos.match_repo import MatchRepo
from infra.db.repos.match_report_repo import MatchReportRepo
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match_report import MatchReport


class ScrapeMatchReport(BaseUseCase):

    def __init__(self, match_id, scraper: BaseScraper, parser: BaseParser):
        self.match_id = match_id
        self.scraper = scraper
        self.parser = parser

    def execute(self):
        match = MatchRepo.find_by_id(self.match_id)
        if match is None:
            raise ValueError("Match not found")
        try:
            html = self.scraper.scrape(match.get_url().replace("Show", "MatchReport").replace("Live", "MatchReport"))
        except Exception:
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        home_summary, away_summary = self.parser.parse(html)
        if home_summary is None:
            raise ValueError("Could not parse HTML")

        self._insert_data(match, home_summary)
        self._insert_data(match, away_summary)

    def _insert_data(self, match, team_summary):
        for report_type in team_summary:
            for report in team_summary[report_type]:
                try:
                    MatchReportRepo.create(
                        MatchReport(match=match,
                                    team=match.home_team_id,
                                    report=report,
                                    type=report_type,
                                    match_id=match.get_id(),
                                    team_id=match._home_team_id
                        ))
                except IntegrityError:
                    db_session.rollback()
                    print("This match report already exists. Continuing...")