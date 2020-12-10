from datetime import datetime, timedelta

from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_league_repo import BaseLeagueRepo
from data.protocols.db.base_match_player_statistics_repo import BaseMatchPlayerStatisticsRepo
from data.protocols.db.base_match_repo import BaseMatchRepo
from data.protocols.db.base_player_repo import BasePlayerRepo
from data.protocols.requester.base_match_odds_requester import BaseMatchOddsRequester
from data.use_cases.base_use_case import BaseUseCase
from domain.models.league import League
from domain.models.match_odds import MatchOdds
from domain.models.match_player_statistics import MatchPlayerStatistics
from domain.models.match_statistics import MatchStatistics
from domain.models.player import Player
from domain.models.team import Team
from infra.db.connection import DBConnection
from infra.db.repos.match_odds_repo import MatchOddsRepo
from infra.db.repos.match_player_statistics_repo import MatchPlayerStatisticsRepo
from infra.db.repos.match_repo import MatchRepo
from infra.db.repos.match_report_repo import MatchReportRepo
from infra.db.repos.match_statistics_repo import MatchStatisticsRepo
from infra.db.repos.player_repo import PlayerRepo
from infra.parsers.base_parser import BaseParser
from infra.requests.base_get_requester import BaseGetRequester
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match_report import MatchReport


class RequestMatchOdds(BaseUseCase):

    def __init__(self, league_name, requester: BaseMatchOddsRequester, league_repository: BaseLeagueRepo,
                 match_odds_repository: MatchOddsRepo, match_repository: MatchRepo):
        self.league_name = league_name
        self.requester = requester
        self.league_repository = league_repository
        self.match_repository = match_repository
        self.match_odds_repository = match_odds_repository

    def execute(self):
        """
        Scrapes the player statistics data of a match and updates the database
        """
        league = self.league_repository.find_by_name(self.league_name)
        if league is None:
            raise ValueError("League not found")

        try:
            # Make url right

            response = self.requester.execute(league.get_odds_api_league_key())
            if response.status_code != 200:
                raise Exception("Request was not a success, an error occurred while requesting the api")
            odds_data = response.json()

            if not odds_data["success"]:
                raise Exception("The request to api was not successful")

            self.insert_data(odds_data["data"])
        except Exception:
            raise ValueError("Could not request data, an error occurred while requesting the api")

    def insert_data(self, data):
        print(data)
        for match in data:
            print(match)
            home_team_name = match["home_team"]
            match["teams"].remove(home_team_name)
            try:
                recent_match = self.match_repository.get_most_recent_match(home_team_name, match["teams"][0])
            except Exception as e:
                # Log: Match not found
                continue

            for site in match["sites"]:
                self.match_odds_repository.create(MatchOdds(**{
                       "match_id": int(recent_match[0]),
                       "site_name": site["site_nice"],
                       "home_win": site["odds"]["h2h"][0],
                       "draw": site["odds"]["h2h"][1],
                       "home_loss": site["odds"]["h2h"][2],
                       "last_update": site["last_update"]
                }))
