import json
import sys
from selenium import webdriver

from league_fixtures import get_league_fixtures, parse_league_fixtures
from league_table import get_league_page_html, parse_league_table_data
from match_report import get_match_report_page_html, parse_match_report
from match_statistics import get_match_statistics_page_html, parse_match_statistics
from player_match_statistics import get_player_match_statistics_page_html, parse_player_match_statistics

BASE_URL = "https://whoscored.com"


def get_driver(driver_path):
    """
    Initialize the webdriver with chromedriver.
    :param driver_path: Path to the chromedriver that execute the script
    :return: The driver to navigate and get the html of the page
    """
    try:
        return webdriver.Chrome(executable_path=driver_path)
    except Exception:
        raise FileNotFoundError("Could not execute webdriver. Make sure you provided the correct path to the "
                                "chromedriver")


def pretty_print(elem):
    """
    Formats the dictionary and print it to the console.
    :param elem: Dictionary to be printed
    """
    print(json.dumps(elem, indent=4, sort_keys=True))


def main(driver_path):
    """
    Main function. Execute all the test scripts to scrape the data.
    :param driver_path: Path to the chromedriver that execute the script
    """
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
    match_statistics_home, match_statistics_away = parse_match_statistics(match_statistics_html)

    pretty_print(match_statistics_home)
    pretty_print(match_statistics_away)

    match_report_html = get_match_report_page_html(driver,
                                                   BASE_URL + league_fixtures[0]["url"].replace("Show", "MatchReport"))
    match_report_home, match_report_away = parse_match_report(match_report_html)

    pretty_print(match_report_home)
    pretty_print(match_report_away)

    player_match_statistics_html = get_player_match_statistics_page_html(driver,
                                                                         BASE_URL + league_fixtures[0]["url"].replace(
                                                                             "Show", "LiveStatistics"))
    player_match_statistics = parse_player_match_statistics(player_match_statistics_html)

    pretty_print(player_match_statistics)


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            raise Exception("Please provide a path to the chromedriver")
    except Exception as e:
        print(f"Invalid input: {e}")


