from abc import ABC, abstractmethod

from infra.requests.base_get_requester import BaseGetRequester


class BaseMatchOddsRequester(ABC):

    def __init__(self, requester: BaseGetRequester):
        """
        Constructor of BaseMatchOddsRequester class
        :param requester: Requester class
        """
        self._requester = requester

    @abstractmethod
    def execute(self, url):
        pass
