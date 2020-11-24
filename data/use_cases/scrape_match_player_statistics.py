from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_match_player_statistics_repo import BaseMatchPlayerStatisticsRepo
from data.protocols.db.base_match_repo import BaseMatchRepo
from data.protocols.db.base_player_repo import BasePlayerRepo
from data.use_cases.base_use_case import BaseUseCase
from domain.models.league import League
from domain.models.match_player_statistics import MatchPlayerStatistics
from domain.models.match_statistics import MatchStatistics
from domain.models.player import Player
from domain.models.team import Team
from infra.db.repos.match_player_statistics_repo import MatchPlayerStatisticsRepo
from infra.db.repos.match_repo import MatchRepo
from infra.db.repos.match_report_repo import MatchReportRepo
from infra.db.repos.match_statistics_repo import MatchStatisticsRepo
from infra.db.repos.player_repo import PlayerRepo
from infra.parsers.base_parser import BaseParser
from infra.scrapers.base_scraper import BaseScraper
from domain.models.match_report import MatchReport


class ScrapeMatchPlayerStatistics(BaseUseCase):

    def __init__(self, match_id, scraper: BaseScraper, parser: BaseParser,
                 match_repository: BaseMatchRepo, player_repository: BasePlayerRepo,
                 match_player_statistics_repo: BaseMatchPlayerStatisticsRepo):
        self.match_id = match_id
        self.scraper = scraper
        self.parser = parser
        self.match_repository = match_repository
        self.player_repository = player_repository
        self.match_player_statistics_repo = match_player_statistics_repo


    def execute(self):
        # TODO Check date of the match if is already finished
        match = self.match_repository.find_by_id(self.match_id)
        if match is None:
            raise ValueError("Match not found")
        try:
            html = self.scraper.scrape(match.get_url().replace("Show", "LiveStatistics")
                                       .replace("Live", "LiveStatistics"))
        except Exception:
            raise ValueError("Could not scrape data, an error occurred while getting the html data")

        players_data = self.parser.parse(html)
        if players_data is None:
            raise ValueError("Could not parse HTML")

        self._insert_data(match, match._home_team_id, players_data["home"])
        self._insert_data(match, match._away_team_id, players_data["away"])
        # self._insert_data(match, away_team)

    def _insert_data(self, match, team_id, players):
        for player_index in players:
            try:
                player_summary = players[player_index]
                player_summary["match_id"] = match.get_id()
                player_summary["team_id"] = team_id
                if player_summary["rating"] == "-":
                    player_summary["rating"] = None
                player = self.player_repository.find_by_name(team_id, player_summary["player_name"])
                if player is None:
                    try:
                        player = self.player_repository.insert_or_update(Player(team=Team(league=League(1)), **{
                            "name": player_summary["player_name"],
                            "team_id": team_id
                        }))
                    except IntegrityError:
                        raise Exception("Could not update league table because team was not found")
                player_summary["player_id"] = player.get_id()

                self.match_player_statistics_repo.create(MatchPlayerStatistics(
                    match=match,
                    team=team_id,
                    player=player,
                    **player_summary)
                )
            except IntegrityError:
                # db_session.rollback()
                print("This match player statistics already exists. Continuing...")