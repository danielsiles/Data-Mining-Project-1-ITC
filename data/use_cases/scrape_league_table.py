from data.use_cases.base_use_case import BaseUseCase
from infra.db.repos.league_repo import LeagueRepo
from infra.db.repos.league_table_repo import LeagueTableRepo
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.league_table import LeagueTable
from domain.models.team import Team


class ScrapeLeagueTable(BaseUseCase):

    def __init__(self, league_name, scraper: BaseScraper, parser: BaseParser):
        self.league_name = league_name
        self.scraper = scraper
        self.parser = parser

    def execute(self):
        league = LeagueRepo.find_by_name(self.league_name)
        if league is None:
            raise ValueError("The name of the league passed is invalid")
        try:
            html = self.scraper.scrape(league.get_url())
        except Exception:
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        league_table_rows = self.parser.parse(html)
        if league_table_rows is None or len(league_table_rows) == 0:
            raise ValueError("Could not parse HTML")
        print(league_table_rows)
        for league_table_row in league_table_rows:
            league_table_row["league_id"] = league.get_id()
            # TODO Get team ID (somehow)
            league_table_row["team_id"] = 1
            league_table_row["year"] = "2020"

            LeagueTableRepo.update_league_table(LeagueTable(league=league, team=Team(1, league=league),
                                                            **league_table_row))
