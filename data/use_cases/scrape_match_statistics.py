from datetime import datetime, timedelta

from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_match_repo import BaseMatchRepo
from data.protocols.db.base_match_statistics_repo import BaseMatchStatisticsRepo
from data.use_cases.base_use_case import BaseUseCase
from domain.models.match_statistics import MatchStatistics
from infra.db.connection import DBConnection
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper

logging.basicConfig(filename='scrape_match_statistics_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)

class ScrapeMatchStatistics(BaseUseCase):
    def __init__(self, match_id, scraper: BaseScraper, parser: BaseParser,
                 match_repository: BaseMatchRepo, match_statistics_repository: BaseMatchStatisticsRepo):
        """
        Constructor for ScrapeMatchPlayerStatistics use case.
        :param match_id: Match id of the match to get player statistics
        :param scraper: Scraper method to scrape league tables html
        :param parser: Parser method to parse the html scraped
        :param match_repository: Repository class of the matches table
        :param match_statistics_repository: Repository class of the match_statistics table
        """
        self.match_id = match_id
        self.scraper = scraper
        self.parser = parser
        self.match_repository = match_repository
        self.match_statistics_repository = match_statistics_repository

    def execute(self):
        match = self.match_repository.find_by_id(self.match_id)
        if match is None:
            logging.error("Could not parse HTML")
            raise ValueError("Match not found")

        if match.get_date() + timedelta(hours=2) > datetime.now():
            logging.error(f"The match hasn't happened yet: {match.get_date() + timedelta(hours=2)}")
            raise ValueError("The match hasn't happened yet")

        try:
            html = self.scraper.scrape(match.get_url().replace("Show", "Live"))
            logging.info("HTML scraping was successful.")
        
        except Exception:
            logging.error("Could not scrape HTML")
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        home_team, away_team = self.parser.parse(html)
        if home_team is None:
            logging.error("Error while scraping home_team HTML")
            raise ValueError("Could not scrape HTML")

        self._insert_data(match, home_team)
        self._insert_data(match, away_team, is_home=False)

    def _insert_data(self, match, team_summary, is_home=True):
        team_id = match.get_home_team_id()
        if not is_home:
            team_id = match.get_away_team_id()
        try:
            team_summary["match_id"] = match.get_id()
            team_summary["team_id"] = team_id
            self.match_statistics_repository.create(MatchStatistics(**team_summary))
        
        except IntegrityError:
            logging.error(f"match report {team_summary["match_id"]} already exists in DB.")
            DBConnection.get_db_session().rollback()
            print("This match report already exists. Continuing...")
