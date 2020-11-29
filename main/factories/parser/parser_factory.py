from infra.parsers.league_table_parser import LeagueTableParser
from infra.parsers.match_parser import MatchParser
from infra.parsers.match_player_statistics_parser import MatchPlayerStatisticsParser
from infra.parsers.match_report_parser import MatchReportParser
from infra.parsers.match_statistics_parser import MatchStatisticsParser


def make_league_table_parser():
    """
    Factory method to create LeagueTableParser
    :return: Instance of LeagueTableParser
    """
    return LeagueTableParser()


def make_match_parser():
    """
    Factory method to create MatchParser
    :return: Instance of MatchParser
    """
    return MatchParser()


def make_match_player_statistics_parser():
    """
    Factory method to create MatchPlayerStatisticsParser
    :return: Instance of MatchPlayerStatisticsParser
    """
    return MatchPlayerStatisticsParser()


def make_match_report_parser():
    """
    Factory method to create MatchReportParser
    :return: Instance of MatchReportParser
    """
    return MatchReportParser()


def make_match_statistics_parser():
    """
    Factory method to create MatchStatisticsParser
    :return: Instance of MatchStatisticsParser
    """
    return MatchStatisticsParser()
