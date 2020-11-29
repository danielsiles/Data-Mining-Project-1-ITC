import json
import argparse
import datetime
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


def validate_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        raise ValueError("Date format should be MM/DD/YYYY")


def main():
    """
    Main function. Execute all the test scripts to scrape the data.
    """
    possible_leagues = ["Premier League","Serie A","LaLiga","Bundesliga","Ligue 1","Liga NOS","Eredivisie","Premier League","Brasileirão","Major League Soccer","Super Lig","Championship","Premiership","League One","League Two","Superliga","Jupiler Pro League","Super league","Bundesliga II","Champions League","Europa League","UEFA Nations League A"]
   

    parser = argparse.ArgumentParser()
    parser.add_argument('--league', default=False, choices=possible_leagues, help='enter the league you would like to scrape')
    parser.add_argument('--match', default=False,help='enter the match you would like to scrape')
    parser.add_argument('--stat', default=False, action='store_true')
    parser.add_argument('--all', default=False, action='store_true')
    parser.add_argument('--daterange', default=False, help='The date format is the following %m/%d/%Y')

	try:
	    args = parser.parse_args()
	    print(args)
	    league = args.league
	    match = args.match
	    stat = args.stat
	    scrape_all = args.all
	    daterange = args.daterange

	    if daterange is True:
	    	validate_date_format(daterange)
	        daterange = datetime.datetime.strptime(args.daterange, '%m/%d/%Y').strftime('%m/%d/%Y')

	    if scrape_all is True:
	        function_to_scrape_all()

	    elif league is True and match is True and stat is False and scrape_all is False:
	        get_all_matches_from_certain_league(league,match,stat,daterange)

	    elif league is True and match is True and stat is True and scrape_all is False:
	        get_all_matches_from_certain_league_with_stat(league,match,stat,daterange)

	    elif league is True and match is False and stat is False and scrape_all is False:
	        get_all_matches_from_certain_league_no_stat(league,match,stat,daterange)
	        
	    elif league is False and match is True and stat is True and scrape_all is False:
	        get_all_matches_with_stat(league,match,stat,daterange)

	    elif league is False and match is True and stat is False and scrape_all is False:
	        get_all_matches_no_stat(league,match,stat,daterange)

    except ValueError: 
        print('An Error Occured')
        exit()

if __name__ == '__main__':
    main()
