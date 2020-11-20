from config import MATCH_STATISTICS_ID
from infra.scrapers.base_scraper import BaseScraper


class MatchStatisticsScraper(BaseScraper):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def scrape(self):
        """
        Parse the html element that contains data about the match statistics
        :return: Html element scraped by the driver
        """
        self._driver.get(self._url)
        return self._driver.find_element_by_id(MATCH_STATISTICS_ID).get_attribute('innerHTML')
