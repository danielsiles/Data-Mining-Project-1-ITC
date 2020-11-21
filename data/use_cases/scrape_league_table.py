from abc import ABC

from data.use_cases.base_use_case import BaseUseCase
from infra.db.repos.league_repo import LeagueRepo
from infra.db.repos.league_table_repo import LeagueTableRepo
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from models.league_table import LeagueTable
from models.team import Team


class ScrapeLeagueTable(BaseUseCase):

    def __init__(self, league_name, scraper: BaseScraper, parser: BaseParser):
        self.league_name = league_name
        self.scraper = scraper
        self.parser = parser

    def execute(self):
        league = LeagueRepo.get_league_by_name(self.league_name)
        if league is None:
            raise ValueError("The name of the league passed is invalid")
        print(league)
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
        # Save to database

# [{'team_name': 'Chelsea', 'team_url': '/Teams/15/Show/England-Chelsea', 'matches_played': '9', 'win': '5', 'draw': '3', 'loss': '1', 'goal_for': '22', 'goal_against': '10', 'goal_difference': '+12', 'points': '18', 'form': 'wddwww'}, {'team_name': 'Leicester', 'team_url': '/Teams/14/Show/England-Leicester', 'matches_played': '8', 'win': '6', 'draw': '0', 'loss': '2', 'goal_for': '18', 'goal_against': '9', 'goal_difference': '+9', 'points': '18', 'form': 'wllwww'}, {'team_name': 'Tottenham', 'team_url': '/Teams/30/Show/England-Tottenham', 'matches_played': '8', 'win': '5', 'draw': '2', 'loss': '1', 'goal_for': '19', 'goal_against': '9', 'goal_difference': '+10', 'points': '17', 'form': 'dwdwww'}, {'team_name': 'Liverpool', 'team_url': '/Teams/26/Show/England-Liverpool', 'matches_played': '8', 'win': '5', 'draw': '2', 'loss': '1', 'goal_for': '18', 'goal_against': '16', 'goal_difference': '+2', 'points': '17', 'form': 'wldwwd'}, {'team_name': 'Southampton', 'team_url': '/Teams/18/Show/England-Southampton', 'matches_played': '8', 'win': '5', 'draw': '1', 'loss': '2', 'goal_for': '16', 'goal_against': '12', 'goal_difference': '+4', 'points': '16', 'form': 'wwdwww'}, {'team_name': 'Aston Villa', 'team_url': '/Teams/24/Show/England-Aston-Villa', 'matches_played': '7', 'win': '5', 'draw': '0', 'loss': '2', 'goal_for': '18', 'goal_against': '9', 'goal_difference': '+9', 'points': '15', 'form': 'wwwllw'}, {'team_name': 'Everton', 'team_url': '/Teams/31/Show/England-Everton', 'matches_played': '8', 'win': '4', 'draw': '1', 'loss': '3', 'goal_for': '16', 'goal_against': '14', 'goal_difference': '+2', 'points': '13', 'form': 'wwdlll'}, {'team_name': 'Crystal Palace', 'team_url': '/Teams/162/Show/England-Crystal-Palace', 'matches_played': '8', 'win': '4', 'draw': '1', 'loss': '3', 'goal_for': '12', 'goal_against': '12', 'goal_difference': '0', 'points': '13', 'form': 'lldwlw'}, {'team_name': 'Wolverhampton Wanderers', 'team_url': '/Teams/161/Show/England-Wolverhampton-Wanderers', 'matches_played': '8', 'win': '4', 'draw': '1', 'loss': '3', 'goal_for': '8', 'goal_against': '9', 'goal_difference': '-1', 'points': '13', 'form': 'lwwdwl'}, {'team_name': 'Manchester City', 'team_url': '/Teams/167/Show/England-Manchester-City', 'matches_played': '7', 'win': '3', 'draw': '3', 'loss': '1', 'goal_for': '10', 'goal_against': '9', 'goal_difference': '+1', 'points': '12', 'form': 'ldwdwd'}, {'team_name': 'Arsenal', 'team_url': '/Teams/13/Show/England-Arsenal', 'matches_played': '8', 'win': '4', 'draw': '0', 'loss': '4', 'goal_for': '9', 'goal_against': '10', 'goal_difference': '-1', 'points': '12', 'form': 'lwllwl'}, {'team_name': 'West Ham', 'team_url': '/Teams/29/Show/England-West-Ham', 'matches_played': '8', 'win': '3', 'draw': '2', 'loss': '3', 'goal_for': '14', 'goal_against': '10', 'goal_difference': '+4', 'points': '11', 'form': 'wwddlw'}, {'team_name': 'Newcastle United', 'team_url': '/Teams/23/Show/England-Newcastle-United', 'matches_played': '9', 'win': '3', 'draw': '2', 'loss': '4', 'goal_for': '10', 'goal_against': '15', 'goal_difference': '-5', 'points': '11', 'form': 'wldwll'}, {'team_name': 'Manchester United', 'team_url': '/Teams/32/Show/England-Manchester-United', 'matches_played': '7', 'win': '3', 'draw': '1', 'loss': '3', 'goal_for': '12', 'goal_against': '14', 'goal_difference': '-2', 'points': '10', 'form': 'wlwdlw'}, {'team_name': 'Leeds', 'team_url': '/Teams/19/Show/England-Leeds', 'matches_played': '8', 'win': '3', 'draw': '1', 'loss': '4', 'goal_for': '14', 'goal_against': '17', 'goal_difference': '-3', 'points': '10', 'form': 'wdlwll'}, {'team_name': 'Brighton', 'team_url': '/Teams/211/Show/England-Brighton', 'matches_played': '8', 'win': '1', 'draw': '3', 'loss': '4', 'goal_for': '11', 'goal_against': '14', 'goal_difference': '-3', 'points': '6', 'form': 'llddld'}, {'team_name': 'Fulham', 'team_url': '/Teams/170/Show/England-Fulham', 'matches_played': '8', 'win': '1', 'draw': '1', 'loss': '6', 'goal_for': '7', 'goal_against': '15', 'goal_difference': '-8', 'points': '4', 'form': 'lldlwl'}, {'team_name': 'West Bromwich Albion', 'team_url': '/Teams/175/Show/England-West-Bromwich-Albion', 'matches_played': '8', 'win': '0', 'draw': '3', 'loss': '5', 'goal_for': '6', 'goal_against': '17', 'goal_difference': '-11', 'points': '3', 'form': 'dlddll'}, {'team_name': 'Burnley', 'team_url': '/Teams/184/Show/England-Burnley', 'matches_played': '7', 'win': '0', 'draw': '2', 'loss': '5', 'goal_for': '3', 'goal_against': '12', 'goal_difference': '-9', 'points': '2', 'form': 'lldlld'}, {'team_name': 'Sheffield United', 'team_url': '/Teams/163/Show/England-Sheffield-United', 'matches_played': '8', 'win': '0', 'draw': '1', 'loss': '7', 'goal_for': '4', 'goal_against': '14', 'goal_difference': '-10', 'points': '1', 'form': 'lldlll'}]