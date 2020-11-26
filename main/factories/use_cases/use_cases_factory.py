from data.use_cases.scrape_league_matches import ScrapeLeagueMatches
from data.use_cases.scrape_league_table import ScrapeLeagueTable
from data.use_cases.scrape_match_player_statistics import ScrapeMatchPlayerStatistics
from data.use_cases.scrape_match_report import ScrapeMatchReport
from data.use_cases.scrape_match_statistics import ScrapeMatchStatistics
from infra.db.repos.league_repo import LeagueRepo
from infra.db.repos.league_table_repo import LeagueTableRepo
from infra.db.repos.match_player_statistics_repo import MatchPlayerStatisticsRepo
from infra.db.repos.match_repo import MatchRepo
from infra.db.repos.match_report_repo import MatchReportRepo
from infra.db.repos.match_statistics_repo import MatchStatisticsRepo
from infra.db.repos.player_repo import PlayerRepo
from infra.db.repos.team_repo import TeamRepo
from main.factories.parser.parser_factory import make_match_parser, make_league_table_parser, \
    make_match_player_statistics_parser, make_match_report_parser, make_match_statistics_parser
from main.factories.scraper.scraper_factory import make_match_scraper, make_league_table_scraper, \
    make_match_player_statistics_scraper, make_match_report_scraper, make_match_statistics_scraper


def make_scrape_league_matches_use_case(league_name):
    return ScrapeLeagueMatches(league_name, make_match_scraper(), make_match_parser(),
                               LeagueRepo(), MatchRepo(), TeamRepo())


def make_scrape_league_table_use_case(league_name):
    return ScrapeLeagueTable(league_name, make_league_table_scraper(), make_league_table_parser(),
                             LeagueRepo(), TeamRepo(), LeagueTableRepo())


def make_scrape_match_player_statistics_use_case(match_id):
    return ScrapeMatchPlayerStatistics(match_id, make_match_player_statistics_scraper(),
                                       make_match_player_statistics_parser(),
                                       MatchRepo(), PlayerRepo(), MatchPlayerStatisticsRepo())


def make_scrape_match_report_use_case(match_id):
    return ScrapeMatchReport(match_id, make_match_report_scraper(), make_match_report_parser(),
                             MatchRepo(), MatchReportRepo())


def make_scrape_match_statistics_use_case(match_id):
    return ScrapeMatchStatistics(match_id, make_match_statistics_scraper(), make_match_statistics_parser(),
                                 MatchRepo(), MatchStatisticsRepo())
