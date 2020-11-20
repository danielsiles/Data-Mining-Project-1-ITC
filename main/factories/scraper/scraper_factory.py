from config import BASE_URL
from infra.scrapers.driver import Driver
from infra.scrapers.league_table_scraper import LeagueTableScraper
from infra.scrapers.match_player_statistics_scraper import MatchPlayerStatisticsScraper
from infra.scrapers.match_report_scraper import MatchReportScraper
from infra.scrapers.match_scraper import MatchScraper
from infra.scrapers.match_statistics_scraper import MatchStatisticsScraper


def make_league_table_scraper(url):
    print(BASE_URL + url)
    return LeagueTableScraper(Driver.get_driver(), BASE_URL + url)


def make_match_player_statistics_scraper(url):
    return MatchPlayerStatisticsScraper(Driver.get_driver(), BASE_URL + url)


def make_match_report_scraper(url):
    return MatchReportScraper(Driver.get_driver(), BASE_URL + url)


def make_match_scraper(url):
    return MatchScraper(Driver.get_driver(), BASE_URL + url)


def make_match_statistics_scraper(url):
    return MatchStatisticsScraper(Driver.get_driver(), BASE_URL + url)
