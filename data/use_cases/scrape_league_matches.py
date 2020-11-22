import datetime

from sqlalchemy.exc import IntegrityError

from data.use_cases.base_use_case import BaseUseCase
from infra.db.connection import db_session
from infra.db.repos.league_repo import LeagueRepo
from infra.db.repos.match_repo import MatchRepo
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match import Match
from domain.models.team import Team


class ScrapeLeagueMatches(BaseUseCase):

    def __init__(self, league_name, scraper: BaseScraper, parser: BaseParser):
        self.league_name = league_name
        self.scraper = scraper
        self.parser = parser

    def execute(self):
        league = LeagueRepo.find_by_name(self.league_name)
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
            league_match["home_team_id"] = 1
            league_match["away_team_id"] = 1
            del league_match["away_team"]
            del league_match["home_team"]
            league_match["year"] = "2020"
            try:
                league_match["date"] = datetime.datetime.strptime(league_match["date"], "%A, %b %d %Y %H:%M")
                MatchRepo.insert_or_update(
                    Match(league=league, home_team=Team(1, league=league), away_team=Team(1, league=league),
                          **league_match))
            except IntegrityError:
                db_session.rollback()
                print("Match has already been inserted. Continuing...")
