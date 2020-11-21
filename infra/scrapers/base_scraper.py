from abc import ABC, abstractmethod


class BaseScraper(ABC):
    def __init__(self, driver):
        self._driver = driver

    @abstractmethod
    def scrape(self, url):
        pass
