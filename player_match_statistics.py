import json
import time

from bs4 import BeautifulSoup as bs


def get_player_match_statistics_page_html(driver, url):
    driver.get(url)
    driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Offensive").click()
    driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Defensive").click()
    driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Passing").click()
    driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Offensive").click()
    driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Defensive").click()
    driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Passing").click()
    time.sleep(1)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    return html


def parse_player_match_statistics(html):
    soup = bs(html, 'html.parser')
    home_players = {}
    away_players = {}
    types = ["home", "away"]
    type_ids = ["summary", "offensive",
                "defensive", "passing"]

    summary_keys = ["player_name", "shots", "shots_on_target", "key_passes", "pass_success", "aerials_won", "touches", "rating"]
    offensive_keys = ["player_name", "shots", "shots_on_target", "key_passes", "dribbles_won", "fouls_given",
                      "offside_given", "dispossessed", "turnover", "rating"]
    defensive_keys = ["player_name", "tackles", "interceptions", "clearances", "shots_blocked", "fouls_committed",
                      "rating"]
    passing_keys = ["player_name", "key_passes", "passes", "pass_success", "crosses", "cross_success", "long_ball",
                    "long_ball_success", "through_ball", "through_ball_success"]

    for type in types:
        print(type)
        for type_id in type_ids:
            print(type_id)
            table = soup.find(id=f"live-player-{type}-stats").find(id=f"live-player-{type}-{type_id}").find(
                id="player-table-statistics-body")
            rows = table.find_all('tr')
            for index, row in enumerate(rows):
                cols = row.find_all('td')
                players = []
                for p_index, ele in enumerate(cols):
                    player_stat = ele.get_text(" ", strip=True)
                    if p_index == 0:
                        player_number = ele.find("a").find("div").get_text(" ", strip=True)
                        players.append(player_number)
                        player_stat = ele.find("a").find("span").get_text(" ", strip=True)
                    if p_index == 1:
                        continue
                    players.append(player_stat)

                if type == "home":
                    if type_id == "summary":
                        home_players[players[0]] = dict(zip(summary_keys, players[1:]))
                    elif type_id == "offensive":
                        home_players[players[0]].update(dict(zip(offensive_keys, players[1:])))
                    elif type_id == "defensive":
                        home_players[players[0]].update(dict(zip(defensive_keys, players[1:])))
                    elif type_id == "passing":
                        home_players[players[0]].update(dict(zip(passing_keys, players[1:])))

                else:
                    if type_id == "summary":
                        away_players[players[0]] = dict(zip(summary_keys, players[1:]))
                    elif type_id == "offensive":
                        away_players[players[0]].update(dict(zip(offensive_keys, players[1:])))
                    elif type_id == "defensive":
                        away_players[players[0]].update(dict(zip(defensive_keys, players[1:])))
                    elif type_id == "passing":
                        away_players[players[0]].update(dict(zip(passing_keys, players[1:])))

    return home_players, away_players
