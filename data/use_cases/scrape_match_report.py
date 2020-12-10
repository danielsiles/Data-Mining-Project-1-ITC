from datetime import datetime, timedelta

from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_match_repo import BaseMatchRepo
from data.protocols.db.base_match_report_repo import BaseMatchReportRepo
from data.use_cases.base_use_case import BaseUseCase
from infra.db.connection import DBConnection
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match_report import MatchReport



logging.basicConfig(filename='scrape_match_report_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)


class ScrapeMatchReport(BaseUseCase):

    def __init__(self, match_id, scraper: BaseScraper, parser: BaseParser,
                 match_repository: BaseMatchRepo, match_report_repository: BaseMatchReportRepo):
        """
        Constructor for ScrapeMatchReport use case.
        :param match_id: Match id of the match to get the match report
        :param scraper: Scraper method to scrape league tables html
        :param parser: Parser method to parse the html scraped
        :param match_repository: Repository class of the matches table
        :param match_report_repository: Repository class of the match_reports table
        """
        self.match_id = match_id
        self.scraper = scraper
        self.parser = parser
        self.match_repository = match_repository
        self.match_report_repository = match_report_repository

    def execute(self):
        """
        Scrapes the report data of a match and updates the database
        """
        match = self.match_repository.find_by_id(self.match_id)
        if match is None:
            logging.error("Match not found")
            raise ValueError("Match not found")

        if match.get_date() + timedelta(hours=2) > datetime.now():
            logging.error(f"The match hasn't happened yet: {match.get_date() + timedelta(hours=2)}")
            raise ValueError("The match hasn't happened yet")

        try:
            html = self.scraper.scrape(match.get_url().replace("Show", "MatchReport").replace("Live", "MatchReport"))
            logging.info("HTML scraping was successful.")

        except Exception:
            logging.error("Error while scraping HTML")
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        home_summary, away_summary = self.parser.parse(html)
        if home_summary is None:
            logging.error("Error while scraping home_summary HTML")
            raise ValueError("Could not parse home_summary HTML")
            
        self._insert_data(match, home_summary)
        self._insert_data(match, away_summary, is_home=False)

    def _insert_data(self, match, team_summary, is_home=True):
        if is_home:
            team_id = match.get_home_team_id()
        else:
            team_id = match.get_away_team_id()
        for report_type in team_summary:
            for report in team_summary[report_type]:
                try:
                    self.match_report_repository.create(
                        MatchReport(match=match,
                                    team=match.home_team_id,
                                    report=report,
                                    type=report_type,
                                    match_id=match.get_id(),
                                    team_id=team_id
                                    ))
                
                except IntegrityError:
                    # TODO Decouple DBConnection from use case
                    DBConnection.get_db_session().rollback()
                    logging.error(f"Match {match} already exists in DB.")
                    print("This match report already exists. Continuing...")
