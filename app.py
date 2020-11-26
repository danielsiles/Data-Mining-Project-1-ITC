import json

from pip._vendor import requests

from config import BASE_URL
from data.use_cases.scrape_league_table import ScrapeLeagueTable
from data.use_cases.scrape_match_player_statistics import ScrapeMatchPlayerStatistics
from data.use_cases.scrape_match_statistics import ScrapeMatchStatistics
from domain.models.league_table import LeagueTable
from domain.models.match import Match
from domain.models.match_player_statistics import MatchPlayerStatistics
from domain.models.match_report import MatchReport
from domain.models.match_statistics import MatchStatistics
from domain.models.league import League
from domain.models.player import Player
from domain.models.team import Team
from main.factories.parser.parser_factory import make_match_statistics_parser, make_league_table_parser, \
    make_match_player_statistics_parser
from main.factories.scraper.scraper_factory import make_match_statistics_scraper, make_league_table_scraper, \
    make_match_player_statistics_scraper
from main.factories.use_cases.use_cases_factory import make_scrape_league_table_use_case, \
    make_scrape_league_matches_use_case, make_scrape_match_report_use_case


def get_popular_leagues():
    # Gets urls for popular leagues
    with open("popular_leagues.json", "r") as file:
        return json.loads(file.read())


def pretty_print(elem):
    """
    Formats the dictionary and print it to the console.
    :param elem: Dictionary to be printed
    """
    print(json.dumps(elem, indent=4, sort_keys=True))


def main():
    """
    Main function. Execute all the test scripts to scrape the data.
    """
    # x = requests.get("https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/8228/Stages/18685/Show/England-Premier-League-2020-2021")
    # print(x.text)
    # try:
    #     # init_db()
    # except Exception:
    #     raise Exception("Could not connect to database")

    # LeagueTable()
    # Match()
    # MatchStatistics()
    # MatchReport()
    # Player()
    # Team()
    # MatchPlayerStatistics()
    # /Regions/252/Tournaments/2/Seasons/8228/Stages/18685/Fixtures/England-Premier-League
    # leagues_seed()
    # league = get_popular_leagues()[0]
    # make_league_table_parser(make_league_table_scraper(league['url']).scrape()).parse()
    # make_scrape_league_table_use_case("Bundesliga").execute()
    # make_scrape_league_matches_use_case("Premier League").execute()
    make_scrape_match_report_use_case(336).execute()

    # ScrapeLeagueTable("Premier League", make_league_table_scraper(), make_league_table_parser()).execute()
    # ScrapeMatchPlayerStatistics(2, make_match_player_statistics_scraper(), make_match_player_statistics_parser())\
    #     .execute()
    # ScrapeLeagueMatches("Premier League", make_match_scraper(), make_match_parser()).execute()
    # ScrapeMatchReport(2, make_match_report_scraper(), make_match_report_parser()).execute()
    # ScrapeMatchStatistics(2, make_match_statistics_scraper(), make_match_statistics_parser()).execute()
    # GetLeagueTable("Brasileirão", make_league_table_scraper(), make_league_table_parser()).execute()
    # league_table_html = get_league_page_html(driver, BASE_URL + league['url'])
    # league_table = parse_league_table_data(league_table_html)
    #
    # pretty_print(league_table)
    #
    # league_fixtures_html = get_league_fixtures(driver, BASE_URL + league['url'].replace("Show", "Fixtures"))
    # league_fixtures = parse_league_fixtures(league_fixtures_html)
    #
    # pretty_print(league_fixtures)
    #
    # match_statistics_html = get_match_statistics_page_html(driver,
    #                                                        BASE_URL + league_fixtures[0]["url"].replace("Show", "Live"))
    # match_statistics_home, match_statistics_away = parse_match_statistics(match_statistics_html)
    #
    # pretty_print(match_statistics_home)
    # pretty_print(match_statistics_away)
    #
    # match_report_html = get_match_report_page_html(driver,
    #                                                BASE_URL + league_fixtures[0]["url"].replace("Show", "MatchReport"))
    # match_report_home, match_report_away = parse_match_report(match_report_html)
    #
    # pretty_print(match_report_home)
    # pretty_print(match_report_away)
    #
    # player_match_statistics_html = get_player_match_statistics_page_html(driver,
    #                                                                      BASE_URL + league_fixtures[0]["url"].replace(
    #                                                                          "Show", "LiveStatistics"))
    # player_match_statistics = parse_player_match_statistics(player_match_statistics_html)
    #
    # pretty_print(player_match_statistics)


if __name__ == '__main__':
    main()
