import json
import argparse
from infra.db.seeds.leagues_seed import leagues_seed
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


def main():
    """
    Main function. Execute all the test scripts to scrape the data.
    """
    possible_leagues = ["Premier League","Serie A","LaLiga","Bundesliga","Ligue 1","Liga NOS","Eredivisie","Premier League","Brasileirão","Major League Soccer","Super Lig","Championship","Premiership","League One","League Two","Superliga","Jupiler Pro League","Super league","Bundesliga II","Champions League","Europa League","UEFA Nations League A"]
   

    parser = argparse.ArgumentParser()
    parser.add_argument('--league', default='', choices = possible_leagues, help='enter the league you would like to scrape')
    parser.add_argument('--fixture', default='',help='enter the match you would like to scrape')
    args = parser.parse_args()
    print(args)

    try:
        league = str(args.league)
        fixture = str(args.fixture)

	    if len(league) > 1:
	    	leagues_seed()
	    	make_scrape_league_table_use_case(league).execute()

	   	elif len(fixture) > 1:
	   		make_scrape_match_player_statistics_use_case(fixture).execute()

	   	elif len(league) > 1 and len(fixture) > 1:
	   		leagues_seed()
	   		make_scrape_league_table_use_case(league).execute()
	   		make_scrape_match_player_statistics_use_case(fixture).execute()

    except ValueError: 
        print('An Error Occured')
        exit()
        
if __name__ == '__main__':
    main()
