from infra.parsers.league_table_parser import LeagueTableParser
from infra.parsers.match_parser import MatchParser
from infra.parsers.match_player_statistics_parser import MatchPlayerStatisticsParser
from infra.parsers.match_report_parser import MatchReportParser
from infra.parsers.match_statistics_parser import MatchStatisticsParser


def make_league_table_parser(html):
    return LeagueTableParser(html)


def make_match_parser(html):
    return MatchParser(html)


def make_match_player_statistics_parser(html):
    return MatchPlayerStatisticsParser(html)


def make_match_report_parser(html):
    return MatchReportParser(html)


def make_match_statistics_parser(html):
    return MatchStatisticsParser(html)
