import time
from random import random

from config import PLAYER_STATISTICS_HOME_ID, PLAYER_STATISTICS_AWAY_ID, PLAYER_STATISTICS_OFFENSIVE_TAB_NAME, \
    PLAYER_STATISTICS_DEFENSIVE_TAB_NAME, PLAYER_STATISTICS_PASSING_TAB_NAME
from infra.scrapers.base_scraper import BaseScraper


class MatchPlayerStatisticsScraper(BaseScraper):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def scrape(self):
        """
        Get the html page with the player statistics of a match
        :return: Html element scraped by the driver
        """
        self._driver.get(self._url)
        self._click_player_match_statistics_tabs(PLAYER_STATISTICS_HOME_ID)
        self._click_player_match_statistics_tabs(PLAYER_STATISTICS_AWAY_ID)
        html = self._driver.execute_script("return document.documentElement.outerHTML;")
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