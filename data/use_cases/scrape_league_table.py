from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_league_repo import BaseLeagueRepo
from data.protocols.db.base_league_table_repo import BaseLeagueTableRepo
from data.protocols.db.base_team_repo import BaseTeamRepo
from data.use_cases.base_use_case import BaseUseCase
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.league_table import LeagueTable
from domain.models.team import Team

logging.basicConfig(filename='scrape_league_table_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)


class ScrapeLeagueTable(BaseUseCase):

    def __init__(self, league_name, scraper: BaseScraper, parser: BaseParser,
                 league_repository: BaseLeagueRepo, team_repository: BaseTeamRepo,
                 league_table_repository: BaseLeagueTableRepo):
        """
        Constructor for ScrapeLeagueTable use case.
        :param league_name: Name of the league to scrape the table.
        :param scraper: Scraper method to scrape league tables html
        :param parser: Parser method to parse the html scraped
        :param league_repository: Repository class of the leagues table
        :param team_repository: Repository class of the teams table
        :param league_table_repository: Repository class of the tables table
        """
        self.league_name = league_name
        self.scraper = scraper
        self.parser = parser
        self.league_repository = league_repository
        self.team_repository = team_repository
        self.league_table_repository = league_table_repository

    def execute(self):
        """
        Scrapes the table data of the league with name self.league_name and update the database
        """
        league = self.league_repository.find_by_name(self.league_name)
        if league is None:
            logging.error("The name of the league passed is invalid")
            raise ValueError("The name of the league passed is invalid")
        try:
            html = self.scraper.scrape(league.get_url())
            logging.info("HTML scraping was successful.")
        
        except Exception:
            logging.error("HTML scraping was unsuccessful.")
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        league_table_rows, league_year = self.parser.parse(html)
        if league_table_rows is None or len(league_table_rows) == 0:
            logging.error(f"HTML scraping was unsuccessful for league_table_rows: {league_table_rows}")
            raise ValueError("Could not parse HTML")

        print(league_table_rows)
        for league_table_row in league_table_rows:
            league_table_row["league_id"] = league.get_id()
            team = self.team_repository.find_by_name(league.get_id(), league_table_row["team_name"])
            if team is None:
                try:
                    team = self.team_repository.insert_or_update(Team(league=league, **{
                        "name": league_table_row["team_name"],
                        "league_id": league_table_row["league_id"],
                        "url": league_table_row["team_url"]
                    }))
                    logging.info(f"{league_table_row} was successfuly processed.")

                except IntegrityError:
                    logging.error(f"Could not update league table in db: {league_table_row}")
                    raise Exception("Could not update league table because team was not found")

            league_table_row["team_id"] = team.get_id()
            league_table_row["year"] = league_year

            self.league_table_repository.update_league_table(LeagueTable(league=league, team=team, **league_table_row))
