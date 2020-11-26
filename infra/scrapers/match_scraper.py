from config import BASE_URL
from infra.scrapers.base_scraper import BaseScraper


class MatchScraper(BaseScraper):
    def __init__(self, driver):
        super().__init__(driver)

    def scrape(self, url):
        """
        Get the html page of all fixtures of a league
        :return: Html element scraped by the driver
        """
        self._driver.get(BASE_URL + url)
        return self._driver.execute_script("return document.documentElement.outerHTML;")


