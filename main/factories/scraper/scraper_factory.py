from config import BASE_URL
from infra.scrapers.driver import Driver
from infra.scrapers.league_table_scraper import LeagueTableScraper
from infra.scrapers.match_player_statistics_scraper import MatchPlayerStatisticsScraper
from infra.scrapers.match_report_scraper import MatchReportScraper
from infra.scrapers.match_scraper import MatchScraper
from infra.scrapers.match_statistics_scraper import MatchStatisticsScraper


def make_league_table_scraper():
    return LeagueTableScraper(Driver.get_driver())


def make_match_player_statistics_scraper():
    return MatchPlayerStatisticsScraper(Driver.get_driver())


def make_match_report_scraper():
    return MatchReportScraper(Driver.get_driver())


def make_match_scraper():
    return MatchScraper(Driver.get_driver())


def make_match_statistics_scraper():
    return MatchStatisticsScraper(Driver.get_driver())
