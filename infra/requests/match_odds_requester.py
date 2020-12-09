from config import BASE_URL, ODDS_API_URL
from data.protocols.requester.base_match_odds_requester import BaseMatchOddsRequester


class MatchOddsRequester(BaseMatchOddsRequester):
    def __init__(self, requester):
        super().__init__(requester)

    def execute(self, url):
        """
        Makes a get requests to the endpoint and parses the result
        :return: Json data returned by the api's endpoint
        """
        return self._requester.get(ODDS_API_URL + url)

