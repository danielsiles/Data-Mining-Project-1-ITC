import logging
import time
from random import random
from selenium.webdriver.support import expected_conditions as cond

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config import PLAYER_STATISTICS_HOME_ID, PLAYER_STATISTICS_AWAY_ID, PLAYER_STATISTICS_OFFENSIVE_TAB_NAME, \
    PLAYER_STATISTICS_DEFENSIVE_TAB_NAME, PLAYER_STATISTICS_PASSING_TAB_NAME, BASE_URL
from infra.scrapers.base_scraper import BaseScraper


logging.basicConfig(filename='match_player_statistics_scraper_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)


class MatchPlayerStatisticsScraper(BaseScraper):
    def __init__(self, driver):
        super().__init__(driver)

    def scrape(self, url):
        """
        Get the html page with the player statistics of a match
        :return: Html element scraped by the driver
        """
        self._driver.get(BASE_URL + url)
        # self._click_player_match_statistics_tabs(PLAYER_STATISTICS_HOME_ID)
        # self._click_player_match_statistics_tabs(PLAYER_STATISTICS_AWAY_ID)
        try:
            element = WebDriverWait(self._driver, 10).until(
                cond.presence_of_element_located((By.CSS_SELECTOR, "#player-table-statistics-body > tr > td"))
            )
            print(f"Scrape of {element} succesful.")
            logging.info(f"Scrape of {url}: succesful.")

        except Exception as e:
            print(f"Error while Scraping {url}: {e}")
            logging.error(f"Error while Scraping {url}: {e}")
        html = self._driver.execute_script("return document.documentElement.outerHTML;")
        self._driver.delete_all_cookies()
        self._driver.set_window_size(800, 800)
        self._driver.set_window_position(0, 0)
        return html

    def _click_player_match_statistics_tabs(self, tab_id):
        """
        Clicks on all of tabs of id tab_id inside of the page of match_statistics
        :param tab_id: The id of the tab in the page to be clicked
        """
        self._driver.find_element_by_id(tab_id).find_element_by_link_text(
            PLAYER_STATISTICS_OFFENSIVE_TAB_NAME).click()
        time.sleep(random())
        self._driver.find_element_by_id(tab_id).find_element_by_link_text(
            PLAYER_STATISTICS_DEFENSIVE_TAB_NAME).click()
        time.sleep(random())
        self._driver.find_element_by_id(tab_id).find_element_by_link_text(
            PLAYER_STATISTICS_PASSING_TAB_NAME).click()
        time.sleep(3)
