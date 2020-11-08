
# def get_team_page_html(url):
#     driver = get_driver(url)
#     driver.find_element_by_id("top-team-stats-options").find_element_by_link_text("Defensive").click()
#     driver.find_element_by_id("top-team-stats-options").find_element_by_link_text("Offensive").click()
#     driver.find_element_by_id("team-squad-stats-options").find_element_by_link_text("Defensive").click()
#     driver.find_element_by_id("team-squad-stats-options").find_element_by_link_text("Offensive").click()
#     driver.find_element_by_id("team-squad-stats-options").find_element_by_link_text("Passing").click()
#     html = driver.execute_script("return document.documentElement.outerHTML;")
#     return html


# def get_league_page_html(url):
#     driver = get_driver(url)
#     html = driver.execute_script("return document.documentElement.outerHTML;")
#     return html

# NOT USING
# def get_team_fixtures_page_html(url):
#     driver = get_driver(url)
#     html = driver.execute_script("return document.documentElement.outerHTML;")
#     return html


# def get_match_report_page_html(url):
#     driver = get_driver(url)
#     html = driver.execute_script("return document.documentElement.outerHTML;")
#     return html


# def get_match_statistics_page_html(url):
#     driver = get_driver(url)
#     element = driver.find_element_by_id('live-match').get_attribute('innerHTML')
#     return element


# def get_player_match_statistics_page_html(url):
#     driver = get_driver(url)
#     driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Offensive").click()
#     driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Defensive").click()
#     driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Passing").click()
#     driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Offensive").click()
#     driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Defensive").click()
#     driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Passing").click()
#     html = driver.execute_script("return document.documentElement.outerHTML;")
#     return html


# def get_team_league_table_data(table, row_keys):
#     data = []
#
#     team_stats_summary = table.find_all("tr")
#     for ts in team_stats_summary[1:]:
#         league_row = []
#         team_league_statistics_row = ts.find_all("td")
#         league_name = team_league_statistics_row[0].find('a')
#         if league_name is None:
#             break
#         league_row.append(league_name.find(text=True, recursive=False))
#         for td in team_league_statistics_row[1:]:
#             if td.has_attr('class') and len(td['class']) > 0 and td['class'][0] == 'aaa':
#                 league_row.append(td.find("span", class_="yellow-card-box").text)
#                 league_row.append(td.find("span", class_="red-card-box").text)
#             else:
#                 league_row.append(td.text)
#         data.append(dict(zip(row_keys, league_row)))
#
#     return data


# def parse_team_league_stats(html):
#     soup = bs(html, 'html.parser')
#     team_league_statistics = []
#
#     team_league_summary_table = soup.find("div", id="top-team-stats-summary")
#     team_league_offensive_table = soup.find("div", id="top-team-stats-offensive")
#     team_league_defensive_table = soup.find("div", id="top-team-stats-defensive")
#
#     summary_row_keys = ["league_name", "matches", "goals", "shots_per_game", "yellow_cards", "red_cards", "possessions",
#                         "pass_precision", "aerials_won"]
#     team_league_summary_data = get_team_league_table_data(team_league_summary_table.find("table"), summary_row_keys)
#
#     offensive_row_keys = ["league_name", "matches", "shots_per_game", "shots_on_target_per_game",
#                           "dribble_won_per_game", "fouls_given_per_game"]
#     team_league_offensive_data = get_team_league_table_data(team_league_offensive_table.find("table"),
#                                                             offensive_row_keys)
#
#     defensive_row_keys = ["league_name", "matches", "shots_conceded_per_game", "tackles_per_game",
#                           "interceptions_per_game", "fouls_per_game", "offsides_given_per_game"]
#     team_league_defensive_data = get_team_league_table_data(team_league_defensive_table.find("table"),
#                                                             defensive_row_keys)
#     print(team_league_summary_data)
#     print(team_league_offensive_data)
#     print(team_league_defensive_data)

# Not using
# def parse_team_fixtures(html):
#     soup = bs(html, 'html.parser')
#     table = soup.find(id="team-fixtures").find(class_="divtable-body")
#     data = []
#     fixtures = table.find_all('div', class_="divtable-row")
#     for fixture in fixtures:
#         fixture_data = []
#         for i, ele in enumerate(fixture.find_all('div')):
#             if i == 0 or (3 < i < 11) or i == 14:
#                 continue
#             red_card = ele.find('span', class_="rcard")
#             if red_card is not None:
#                 red_card.decompose()
#             fixture_data.append(ele.get_text(" ", strip=True))
#         row_keys = ["win", "championship", "date", "home_team", "result", "away_team"]
#         data.append(dict(zip(row_keys, fixture_data)))
#     print(data)


# Not using
# def parse_player_stats(html):
#     soup = bs(html, 'html.parser')
#     table = soup.find("table", id="top-player-stats-summary-grid")
#     data = []
#     rows = table.find_all('tr')
#     for index, row in enumerate(rows):
#         if index == 0:
#             continue
#         cols = row.find_all('td')
#         players = []
#         for p_index, ele in enumerate(cols):
#             player_stat = ele.get_text(" ", strip=True)
#             if p_index == 0:
#                 player_stat = ele.find("a").find("span").get_text(" ", strip=True)
#             if p_index == 1:
#                 continue
#             players.append(player_stat)
#         row_keys = ["name", "centimeters", "kilos", "matches", "minutes_played", "goals", "assists", "yellow_cards",
#                     "red_cards", "shots_per_game", "pass_success", "aerial_won_per_game", "man_of_the_match"]
#         data.append(dict(zip(row_keys, players)))
#     print(data)


# def parse_league_table_data(html):
#     soup = bs(html, 'html.parser')
#     tournament_table = soup.find("div", class_="tournament-standings-table")
#     league_table_rows = tournament_table.find("tbody", class_="standings")
#     tr = []
#     for league_table_row in league_table_rows:
#         team_infos = league_table_row.find_all('td')
#         tr_info = []
#         team_name = team_infos[0]
#         tr_info.append(team_name.a.text)
#         tr_info.append(team_name.a["href"])
#         for team_info in team_infos[1:]:
#             tr_info.append(team_info.text)
#         row_keys = ["team_name", "team_url", "matches_played", "win",
#                     "draw", "loss", "goal_for", "goal_against",
#                     "goal_difference", "points"" form"
#                     ]
#
#         tr.append(dict(zip(row_keys, tr_info)))
#
#     print(json.dumps(tr, indent=4, sort_keys=True))


# def parse_match_report(html):
#     soup = bs(html, 'html.parser')
#     match_summary_table = soup.find("table", class_="matchstory")
#     rows = match_summary_table.find_all('tr')
#
#     home_summary = {"strengths": [], "weaknesses": [], "styles": []}
#     away_summary = {"strengths": [], "weaknesses": [], "styles": []}
#     types = ["strengths", "weaknesses", "styles"]
#     type_id = -1
#     for index, row in enumerate(rows):
#         if index == 0:
#             continue
#
#         if row['class'][0] == "matchstory-typeheader":
#             type_id += 1
#             continue
#
#         teams_data = row.find_all('td')
#         home_data = teams_data[0].get_text(" ", strip=True)
#         away_data = teams_data[1].get_text(" ", strip=True)
#         if home_data != '':
#             home_summary[types[type_id]].append(home_data)
#         if away_data != '':
#             away_summary[types[type_id]].append(away_data)
#
#     print(home_summary)
#     print(away_summary)


# def parse_match_statistics(html):
#     soup = bs(html, 'html.parser')
#     home_team = []
#     away_team = []
#     match_result = soup.find(id="match-centre-header").find(class_="score").get_text(" ", strip=True).split(":")
#     home_team.append(match_result[0].replace(" ", ""))
#     away_team.append(match_result[1].replace(" ", ""))
#     match_statistics_table = soup.find(id="match-centre-stats").find("ul").find_all(class_="match-centre-stat")
#     for row in match_statistics_table:
#         stats = row.find_all("span", class_="match-centre-stat-value")
#         home_team.append(stats[0].get_text(" ", strip=True))
#         away_team.append(stats[1].get_text(" ", strip=True))
#     row_keys = ["goals", "ratings", "shots", "possession", "pass_success", "dribles",
#                 "aerials_won", "tackles", "corners", "dispossessed"]
#
#     print(dict(zip(row_keys, home_team)))
#     print(dict(zip(row_keys, away_team)))


# live-player-home-stats
# live-player-away-stats
# def parse_player_match_statistics(html):
#     soup = bs(html, 'html.parser')
#     home_players = []
#     away_players = []
#     types = ["home", "away"]
#     team_ids = ["live-player-home-stats", "live-player-away-stats"]
#     type_ids = ["summary", "offensive",
#                 "defensive", "passing"]
#     for type in types:
#         print(type)
#         for type_id in type_ids:
#             print(type_id)
#             table = soup.find(id=f"live-player-{type}-stats").find(id=f"live-player-{type}-{type_id}").find(
#                 id="player-table-statistics-body")
#             rows = table.find_all('tr')
#             for index, row in enumerate(rows):
#                 cols = row.find_all('td')
#                 players = []
#                 for p_index, ele in enumerate(cols):
#                     player_stat = ele.get_text(" ", strip=True)
#                     if p_index == 0:
#                         player_stat = ele.find("a").find("span").get_text(" ", strip=True)
#                     if p_index == 1:
#                         continue
#                     players.append(player_stat)
#                 print(players)


# NEW CODEEEEEE


# def get_league_fixtures(driver, url):
#     driver.get(url)
#     return driver.execute_script("return document.documentElement.outerHTML;")
#
#
# def parse_league_fixtures(html):
#     soup = bs(html, 'html.parser')
#     table = soup.find(id="tournament-fixture")
#     fixtures = table.find_all("div", class_="divtable-row")
#     curr_date = ""
#     matches = []
#     for fixture in fixtures:
#         header = fixture.find(class_="divtable-header")
#         if header is not None:
#             curr_date = header.get_text(" ", strip=True)
#             continue
#
#         match_time = fixture.find(class_="time").get_text(" ", strip=True)
#         links = fixture.find_all("a")
#         curr_link = "#"
#         for link in links:
#             if "Matches" in str(link) or "Live" in str(link):
#                 print(link)
#                 curr_link = link
#         matches.append({
#             "date": curr_date + " " + match_time,
#             "result": curr_link.get_text(" ", strip=True),
#             "link": curr_link["href"]
#         })
#     print(matches)
#

import json
import os
from selenium import webdriver

from player_match_statistics import get_player_match_statistics_page_html, parse_player_match_statistics

BASE_URL = "https://whoscored.com"

def get_driver():
    return webdriver.Chrome(executable_path=os.path.abspath('') + '/chromedriver')

def main():
    # Opens the browser for selenium
    driver = get_driver()

    # Gets urls for popular leagues
    # with open("popular_leagues.json", "r") as file:
    #     leagues = json.loads(file.read())
    #     for league in leagues:
    #         print(league["league_name"])
    #         print(BASE_URL + league["url"])

    # Parsing player match statistics
    player_match_statistics_html = get_player_match_statistics_page_html(driver,
        "https://www.whoscored.com/Matches/1457748/LiveStatistics/Brazil-Brasileir%C3%A3o-2020-Palmeiras-Atletico-MG")
    print(parse_player_match_statistics(player_match_statistics_html))


if __name__ == '__main__':
    main()
    # with open("leagues.json", "r") as file:
    #     countries = json.loads(file.read())
    #     for country in countries:
    #         for league in country["tournaments"]:
    #             print(league['url'])
    # # Parsing league table
    # league_page_html = get_league_page_html("https://www.whoscored.com/Regions/31/Tournaments/95/Brazil-Brasileir%C3"
    #                                         "%A3o")
    # parse_league_table_data(league_page_html)
    #
    # # Parsing team page
    # team_page_html = get_team_page_html("https://www.whoscored.com/Teams/1239/Show/Brazil-Flamengo")
    # parse_team_league_stats(team_page_html)
    # parse_player_stats(team_page_html)

    # Parsing team fixtures
    # team_fixtures_html = get_team_fixtures_page_html("https://www.whoscored.com/Teams/1239/Fixtures/Brazil-Flamengo")
    # parse_team_fixtures(team_fixtures_html)

    # Parsing match summary
    # match_report_html = get_match_report_page_html("https://www.whoscored.com/Matches/1457734/MatchReport/Brazil-Brasileir%C3%A3o-2020-Corinthians-Flamengo")
    # parse_match_report(match_report_html)

    # Parsing match statistics
    # match_statistics_html = get_match_statistics_page_html("https://www.whoscored.com/Matches/1457748/Live/Brazil-Brasileir%C3%A3o-2020-Palmeiras-Atletico-MG")
    # parse_match_statistics(match_statistics_html)

    # Parsing player match statistics
    # player_match_statistics_html = get_player_match_statistics_page_html("https://www.whoscored.com/Matches/1457748/LiveStatistics/Brazil-Brasileir%C3%A3o-2020-Palmeiras-Atletico-MG")
    # parse_player_match_statistics(player_match_statistics_html)



    # NEW CODEEEE

    # driver = get_driver()
    # html = get_league_fixtures(driver,
    #                            "https://www.whoscored.com/Regions/31/Tournaments/95/Seasons/8158/Stages/18472/Fixtures/Brazil-Brasileir%C3%A3o-2020")
    # parse_league_fixtures(html)