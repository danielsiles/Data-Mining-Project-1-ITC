from config import BASE_URL
from infra.scrapers.driver import Driver
from infra.scrapers.league_table_scraper import LeagueTableScraper
from infra.scrapers.match_player_statistics_scraper import MatchPlayerStatisticsScraper
from infra.scrapers.match_report_scraper import MatchReportScraper
from infra.scrapers.match_scraper import MatchScraper
from infra.scrapers.match_statistics_scraper import MatchStatisticsScraper


def make_league_table_scraper():
    """
    Factory method to create LeagueTableScraper
    :return: Instance of LeagueTableScraper
    """
    return LeagueTableScraper(Driver.get_driver())


def make_match_player_statistics_scraper():
    """
    Factory method to create MatchPlayerStatisticsScraper
    :return: Instance of MatchPlayerStatisticsScraper
    """
    return MatchPlayerStatisticsScraper(Driver.get_driver())


def make_match_report_scraper():
    """
    Factory method to create MatchReportScraper
    :return: Instance of MatchReportScraper
    """
    return MatchReportScraper(Driver.get_driver())


def make_match_scraper():
    """
    Factory method to create MatchScraper
    :return: Instance of MatchScraper
    """
    return MatchScraper(Driver.get_driver())


def make_match_statistics_scraper():
    """
    Factory method to create MatchStatisticsScraper
    :return: Instance of MatchStatisticsScraper
    """
    return MatchStatisticsScraper(Driver.get_driver())
