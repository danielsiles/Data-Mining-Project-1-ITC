import datetime

from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_league_repo import BaseLeagueRepo
from data.protocols.db.base_match_repo import BaseMatchRepo
from data.protocols.db.base_team_repo import BaseTeamRepo
from data.use_cases.base_use_case import BaseUseCase
from infra.db.connection import DBConnection
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match import Match
from domain.models.team import Team


class ScrapeLeagueMatches(BaseUseCase):

    def __init__(self, league_name, scraper: BaseScraper, parser: BaseParser,
                 league_repository: BaseLeagueRepo, match_repository: BaseMatchRepo,
                 team_repository: BaseTeamRepo):
        """
        Constructor for ScrapeLeagueMatches use case.
        :param league_name: Name of the league to scrape the matches.
        :param scraper: Scraper method to scrape league tables html
        :param parser: Parser method to parse the html scraped
        :param league_repository: Repository class of the leagues tables
        :param match_repository: Repository class of the matches tables
        :param team_repository: Repository class of the teams tables
        """
        self.league_name = league_name
        self.scraper = scraper
        self.parser = parser
        self.league_repository = league_repository
        self.match_repository = match_repository
        self.team_repository = team_repository

    def execute(self):
        """
        Scrapes the matches data of the league with name self.league_name and update the database
        """
        league = self.league_repository.find_by_name(self.league_name)
        if league is None:
            raise ValueError("The name of the league passed is invalid")

        print(league.get_url())
        try:
            html = self.scraper.scrape(league.get_fixture_url())
        except Exception:
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        league_matches = self.parser.parse(html)
        print(league_matches)
        if league_matches is None or len(league_matches) == 0:
            raise ValueError("Could not parse HTML")
        for league_match in league_matches:
            league_match["league_id"] = league.get_id()
            league_match["home_team_id"] = self.team_repository.find_by_name(league.get_id(),
                                                                             league_match["home_team"]).get_id()
            league_match["away_team_id"] = self.team_repository.find_by_name(league.get_id(),
                                                                             league_match["away_team"]).get_id()
            del league_match["away_team"]
            del league_match["home_team"]
            league_match["year"] = "2020"
            try:
                league_match["date"] = datetime.datetime.strptime(league_match["date"], "%A, %b %d %Y %H:%M")
                self.match_repository.insert_or_update(
                    Match(league=league, home_team=Team(1, league=league), away_team=Team(1, league=league),
                          **league_match))
            except IntegrityError:
                # TODO Decouple DBConnection from use case
                DBConnection.get_db_session().rollback()
                print("Match has already been inserted. Continuing...")
