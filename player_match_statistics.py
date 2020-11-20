import time
from random import random

from bs4 import BeautifulSoup as bs

from config import PLAYER_STATISTICS_HOME_ID, PLAYER_STATISTICS_OFFENSIVE_TAB_NAME, \
    PLAYER_STATISTICS_DEFENSIVE_TAB_NAME, PLAYER_STATISTICS_PASSING_TAB_NAME, PLAYER_STATISTICS_AWAY_ID, \
    PLAYER_STATISTICS_TABLE_ID


def get_player_match_statistics_page_html(driver, url):
    """
    Get the html page with the player statistics of a match
    :param driver: driver to navigate to url and execute script
    :param url: A url of the website that will be scraped by the driver
    :return: Html element scraped by the driver
    """
    driver.get(url)
    click_player_match_statistics_tabs(driver, PLAYER_STATISTICS_HOME_ID)
    click_player_match_statistics_tabs(driver, PLAYER_STATISTICS_AWAY_ID)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    return html

#
# def click_player_match_statistics_tabs(driver, tab_id):
#     """
#     Clicks on all of tabs of id tab_id inside of the page of match_statistics
#     :param driver: driver to click the tabs on the page
#     :param tab_id: The id of the tab in the page to be clicked
#     """
#     driver.find_element_by_id(tab_id).find_element_by_link_text(
#         PLAYER_STATISTICS_OFFENSIVE_TAB_NAME).click()
#     time.sleep(random())
#     driver.find_element_by_id(tab_id).find_element_by_link_text(
#         PLAYER_STATISTICS_DEFENSIVE_TAB_NAME).click()
#     time.sleep(random())
#     driver.find_element_by_id(tab_id).find_element_by_link_text(
#         PLAYER_STATISTICS_PASSING_TAB_NAME).click()
#     time.sleep(3)


def parse_player_match_statistics(html):
    """
    Parse the html element that contains data about the players in a match
    :param html: Html element scraped to be parsed
    :return: Statistics about all the players of a match
    """
    # soup = bs(html, 'html.parser')
    # home_players = {}
    # away_players = {}
    #
    # types = ["home", "away"]
    # type_ids = ["summary", "offensive",
    #             "defensive", "passing"]
    #
    # summary_keys = ["player_name", "shots", "shots_on_target", "key_passes", "pass_success", "aerials_won", "touches",
    #                 "rating"]
    # offensive_keys = ["player_name", "shots", "shots_on_target", "key_passes", "dribbles_won", "fouls_given",
    #                   "offside_given", "dispossessed", "turnover", "rating"]
    # defensive_keys = ["player_name", "tackles", "interceptions", "clearances", "shots_blocked", "fouls_committed",
    #                   "rating"]
    # passing_keys = ["player_name", "key_passes", "passes", "pass_success", "crosses", "cross_success", "long_ball",
    #                 "long_ball_success", "through_ball", "through_ball_success"]
    #
    # data = {"home": home_players, "away": away_players}
    # keys = dict(zip(type_ids, [summary_keys, offensive_keys, defensive_keys, passing_keys]))
    # for tp in types:
    #     for type_id in type_ids:
    #         table = soup.find(id=f"live-player-{tp}-stats").find(id=f"live-player-{tp}-{type_id}").find(
    #             id=PLAYER_STATISTICS_TABLE_ID)
    #         rows = table.find_all('tr')
    #         for index, row in enumerate(rows):
    #             cols = row.find_all('td')
    #             players = []
    #             for p_index, ele in enumerate(cols):
    #                 player_stat = ele.get_text(" ", strip=True)
    #                 if p_index == 0:
    #                     player_number = ele.find("a").find("div").get_text(" ", strip=True)
    #                     players.append(player_number)
    #                     player_stat = ele.find("a").find("span").get_text(" ", strip=True)
    #                 if p_index == 1:
    #                     continue
    #                 players.append(player_stat)
    #
    #             if players[0] not in data[tp]:
    #                 data[tp][players[0]] = {}
    #             else:
    #                 data[tp][players[0]].update(dict(zip(keys[type_id], players[1:])))
    #
    #             print(data)
    #
    # return data
