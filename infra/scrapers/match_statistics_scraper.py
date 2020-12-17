import logging

from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import MATCH_STATISTICS_ID, BASE_URL
from infra.scrapers.base_scraper import BaseScraper


logging.basicConfig(filename='match_statistics_scraper_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)



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
            print(f"Scrape of {element} succesful.")
            logging.info(f"Scrape of {url}: succesful.")

        except Exception as e:
            print(f"Error while Scraping {url}: {e}")
            logging.error(f"Error while Scraping {url}: {e}")
        self._driver.delete_all_cookies()
        self._driver.set_window_size(800, 800)
        self._driver.set_window_position(0, 0)
        return self._driver.find_element_by_id(MATCH_STATISTICS_ID).get_attribute('innerHTML')
