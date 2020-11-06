import json
import os
import sys
from selenium import webdriver

from league_fixtures import get_league_fixtures, parse_league_fixtures
from league_table import get_league_page_html, parse_league_table_data
from match_report import get_match_report_page_html, parse_match_report
from match_statistics import get_match_statistics_page_html, parse_match_statistics

BASE_URL = "https://whoscored.com"


def get_driver(driver_path):
    return webdriver.Chrome(executable_path=driver_path)


def pretty_print(elem):
    print(json.dumps(elem, indent=4, sort_keys=True))


def main(driver_path):
    # Opens the browser for selenium
    driver = get_driver(driver_path)

    # Gets urls for popular leagues
    with open("popular_leagues.json", "r") as file:
        league = json.loads(file.read())[0]

    league_table_html = get_league_page_html(driver, BASE_URL + league['url'])
    league_table = parse_league_table_data(league_table_html)

    pretty_print(league_table)

    league_fixtures_html = get_league_fixtures(driver, BASE_URL + league['url'].replace("Show", "Fixtures"))
    league_fixtures = parse_league_fixtures(league_fixtures_html)

    pretty_print(league_fixtures)

    match_statistics_html = get_match_statistics_page_html(driver,
                                                           BASE_URL + league_fixtures[0]["url"].replace("Show", "Live"))
    match_statistics = parse_match_statistics(match_statistics_html)

    pretty_print(match_statistics)

    match_report_html = get_match_report_page_html(driver,
                                                   BASE_URL + league_fixtures[0]["url"].replace("Show", "MatchReport"))
    match_report = parse_match_report(match_report_html)

    pretty_print(match_report)


if __name__ == '__main__':
    main(sys.argv[1])
