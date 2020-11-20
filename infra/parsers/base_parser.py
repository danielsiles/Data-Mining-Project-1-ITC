from abc import ABC, abstractmethod


class BaseParser(ABC):
    def __init__(self, html):
        self._html = html

    @abstractmethod
    def parse(self):
        pass
