from abc import ABC, abstractmethod


class BaseScraper(ABC):
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    @abstractmethod
    def scrape(self):
        pass
