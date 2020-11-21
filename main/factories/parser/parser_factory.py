from infra.parsers.league_table_parser import LeagueTableParser
from infra.parsers.match_parser import MatchParser
from infra.parsers.match_player_statistics_parser import MatchPlayerStatisticsParser
from infra.parsers.match_report_parser import MatchReportParser
from infra.parsers.match_statistics_parser import MatchStatisticsParser


def make_league_table_parser():
    return LeagueTableParser()


def make_match_parser():
    return MatchParser()


def make_match_player_statistics_parser():
    return MatchPlayerStatisticsParser()


def make_match_report_parser():
    return MatchReportParser()


def make_match_statistics_parser():
    return MatchStatisticsParser()
