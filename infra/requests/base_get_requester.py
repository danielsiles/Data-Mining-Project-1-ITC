from abc import ABC, abstractmethod


class BaseGetRequester(ABC):

    @abstractmethod
    def get(self, url):
        pass
