import json
import argparse
import datetime

from sqlalchemy import create_engine

from infra.db.connection import DBConnection
from infra.db.repos.league_repo import LeagueRepo
from infra.db.repos.match_repo import MatchRepo
from infra.db.seeds.leagues_seed import leagues_seed
from config import BASE_URL, DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT
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
from infra.scrapers.driver import Driver
from main.factories.parser.parser_factory import make_match_statistics_parser, make_league_table_parser, \
    make_match_player_statistics_parser
from main.factories.scraper.scraper_factory import make_match_statistics_scraper, make_league_table_scraper, \
    make_match_player_statistics_scraper
from main.factories.use_cases.use_cases_factory import make_scrape_league_table_use_case, \
    make_scrape_league_matches_use_case, make_scrape_match_report_use_case, make_scrape_match_statistics_use_case, \
    make_scrape_match_player_statistics_use_case


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


def validate_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        raise ValueError("Date format should be MM/DD/YYYY")


def main():
    """
    Main function. Execute all the test scripts to scrape the data.
    """
    possible_leagues = ["Premier League", "Serie A", "LaLiga", "Bundesliga", "Ligue 1", "Liga NOS", "Eredivisie",
                        "Premier "
                        "League",
                        "Brasileirão", "Major League Soccer", "Super Lig", "Championship", "Premiership", "League One",
                        "League Two", "Superliga", "Jupiler Pro League", "Super league", "Bundesliga II", "Champions "
                                                                                                          "League",
                        "Europa League", "UEFA Nations League A"]

    parser = argparse.ArgumentParser()
    parser.add_argument('--driver', help='seed the database with popular leagues', required=True)
    parser.add_argument('--create_db', action='store_true', help='drop and creates new database with tables')
    parser.add_argument('--seed', action='store_true', help='seed the database with popular leagues')
    parser.add_argument('--populate', action='store_true', help='populate the database with leagues tables and '
                                                                'matches')
    parser.add_argument('--league', default=False,
                        choices=possible_leagues,
                        help='enter the league table you would like to scrape')
    parser.add_argument('--match', action='store_true', default=False, help='enter the match you would like to scrape')
    parser.add_argument('--stat', default=False, action='store_true')
    parser.add_argument('--all', default=False, action='store_true')
    parser.add_argument('--daterange', default=False, help='The date format is the following %m/%d/%Y')

    try:
        args = parser.parse_args()
        print(args)
        driver = args.driver
        create_db = args.create_db
        league = args.league
        match = args.match
        stat = args.stat
        scrape_all = args.all
        date = args.daterange
        seed = args.seed
        populate = args.populate

        Driver.init_driver(driver)
        mr = MatchRepo()
        lr = LeagueRepo()
        if create_db is True:
            engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}',
                                   echo=False,
                                   convert_unicode=True)
            engine.execute(f"DROP DATABASE {DB_NAME}")
            engine.execute(f"CREATE DATABASE {DB_NAME}")
            # leagues_seed()

        if seed is True:
            leagues_seed(populate=populate)

        if date is True:
            validate_date_format(date)
            date = datetime.datetime.strptime(args.daterange, '%Y/%m/%d').strftime('%Y/%m/%d')

        if scrape_all is True:
            leagues_seed(populate=True)
            matches = mr.get_matches()

            for match in matches:
                match = match[0]
                make_scrape_match_statistics_use_case(match.get_id()).execute()
                make_scrape_match_report_use_case(match.get_id()).execute()
                make_scrape_match_player_statistics_use_case(match.get_id()).execute()

        elif league is not False and match is False and stat is False:
            make_scrape_league_table_use_case(str(league)).execute()

        elif league is False and match is not False and stat is False:
            leagues = lr.get_all()
            for league in leagues:
                make_scrape_league_matches_use_case(league.get_name()).execute()

        elif league is not False and match is not False and stat is not False:
            matches = mr.get_matches(league=str(league), date=date)

            for match in matches:
                match = match[0]
                make_scrape_match_statistics_use_case(match.get_id()).execute()
                make_scrape_match_report_use_case(match.get_id()).execute()
                make_scrape_match_player_statistics_use_case(match.get_id()).execute()

        elif league is not False and match is False and stat is False:
            make_scrape_league_table_use_case(str(league)).execute()

    except ValueError:
        print('An Error Occured')
        exit()


if __name__ == '__main__':
    main()
