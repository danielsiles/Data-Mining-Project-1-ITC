from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import MATCH_STATISTICS_ID, BASE_URL
from infra.scrapers.base_scraper import BaseScraper


class MatchStatisticsScraper(BaseScraper):
    def __init__(self, driver):
        super().__init__(driver)

    def scrape(self, url):
        """
        Parse the html element that contains data about the match statistics
        :return: Html element scraped by the driver
        """
        self._driver.get(BASE_URL + url)
        try:
            element = WebDriverWait(self._driver, 10).until(
                cond.presence_of_element_located((By.CLASS_NAME, "match-centre-stat"))
            )
            print("ELEMENTOOO", element)
        except Exception as e:
            print("NAOO ACHOU!!", e)

        return self._driver.find_element_by_id(MATCH_STATISTICS_ID).get_attribute('innerHTML')
