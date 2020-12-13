import logging

from sqlalchemy.exc import IntegrityError

from data.protocols.db.base_league_repo import BaseLeagueRepo
from data.protocols.requester.base_match_odds_requester import BaseMatchOddsRequester
from data.use_cases.base_use_case import BaseUseCase
from domain.models.match_odds import MatchOdds
from infra.db.connection import DBConnection
from infra.db.repos.match_odds_repo import MatchOddsRepo
from infra.db.repos.match_repo import MatchRepo

logging.basicConfig(filename='scrape_league_matches_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)


class RequestMatchOdds(BaseUseCase):

    def __init__(self, league_name, requester: BaseMatchOddsRequester, league_repository: BaseLeagueRepo,
                 match_odds_repository: MatchOddsRepo, match_repository: MatchRepo):
        """
        Constructor for RequestMatchOdds use case.
        :param league_name: Name of the league to scrape the matches.
        :param requester: Request method to make a http request
        :param league_repository: Repository class of the leagues tables
        :param match_repository: Repository class of the matches tables
        :param match_odds_repository: Repository class of the match_odds tables
        """
        self.league_name = league_name
        self.requester = requester
        self.league_repository = league_repository
        self.match_repository = match_repository
        self.match_odds_repository = match_odds_repository

    def execute(self):
        """
        Makes http request to the match odds api and updates the database
        """
        logging.debug(f"Querying league model with name {self.league_name} from the database")
        league = self.league_repository.find_by_name(self.league_name)

        if league is None:
            logging.error("The name of the league passed is invalid")
            raise ValueError("League not found")
        logging.info("League was successfully retrieved from the database.")
        try:
            logging.debug(f"Performing http request with league key {league.get_odds_api_league_key()}")
            response = self.requester.execute(league.get_odds_api_league_key())
            if response.status_code != 200:
                logging.error("Request was not a success, an error occurred while requesting the api")
                raise Exception("Request was not a success, an error occurred while requesting the api")
            logging.info("Request to api was a success")
            logging.debug(f"Parsing text into a json object")
            odds_data = response.json()

            if not odds_data["success"]:
                logging.error("The request to api was not successful")
                raise Exception("The request to api was not successful")
            logging.debug(f"Inserting data into the database")
            self.insert_data(odds_data["data"])
            logging.info(f"Odds data successfully inserted")
        except Exception:
            logging.error("Could not request data, an error occurred while requesting the api")
            raise ValueError("Could not request data, an error occurred while requesting the api")

    def insert_data(self, data):
        """
        Parses the data and inserts it into the database
        :param data: Data requested from the api
        :return:
        """
        for match in data:
            logging.debug(f"Parsing match {match}")
            home_team_name = match["home_team"]
            match["teams"].remove(home_team_name)
            try:
                recent_match = self.match_repository.get_most_recent_match(home_team_name, match["teams"][0])
            except ValueError:
                logging.error("The match was not found")
                continue

            if recent_match is None:
                logging.error(f"The match was not found in the database")
                continue

            logging.debug(f"Match found")

            for site in match["sites"]:
                try:
                    self.match_odds_repository.create(MatchOdds(**{
                           "match_id": int(recent_match[0]),
                           "site_name": site["site_nice"],
                           "home_win": site["odds"]["h2h"][0],
                           "draw": site["odds"]["h2h"][1],
                           "home_loss": site["odds"]["h2h"][2],
                           "last_update": site["last_update"]
                    }))
                except IntegrityError:
                    logging.info("This match odds already exists. Rolling back...")
                    DBConnection.get_db_session().rollback()
