# Main config
API_KEY = "a0f051ecbe12637ec3f97e80eaeb08b7"
ODDS_API_URL = f"https://api.the-odds-api.com/v3/odds/?apiKey={API_KEY}&region=eu&mkt=h2h&sport="
BASE_URL = "https://whoscored.com"

DB_USERNAME = "root"
DB_PASSWORD = "q1w2e3"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "whoscored_db"

# League Fixtures

FIXTURE_TABLE_ID = "tournament-fixture"
FIXTURE_TABLE_ROW = "divtable-row"
FIXTURE_TABLE_HEADER = "divtable-header"

# League table

LEAGUE_YEAR_ID = "seasons"
LEAGUE_TABLE_CLASS = "tournament-standings-table"
LEAGUE_TABLE_ROW_CLASS = "standings"

# Match Report

MATCH_REPORT_SUMMARY_TABLE_CLASS = "matchstory"
MATCH_REPORT_SUMMARY_TABLE_HEADER_CLASS = "matchstory-typeheader"

# Match Statistics

MATCH_STATISTICS_ID = "live-match"
MATCH_STATISTICS_RESULT_ID = "match-centre-header"
MATCH_STATISTICS_SCORE_CLASS = "score"
MATCH_STATISTICS_TABLE_ID = "match-centre-stats"
MATCH_STATISTICS_TABLE_ROW_CLASS = "match-centre-stat"
MATCH_STATISTICS_TABLE_ROW_VALUE_CLASS = "match-centre-stat-value"

# Player statistics

PLAYER_STATISTICS_HOME_ID = "live-player-home-options"
PLAYER_STATISTICS_AWAY_ID = "live-player-away-options"
PLAYER_STATISTICS_OFFENSIVE_TAB_NAME = "Offensive"
PLAYER_STATISTICS_DEFENSIVE_TAB_NAME = "Defensive"
PLAYER_STATISTICS_PASSING_TAB_NAME = "Passing"
PLAYER_STATISTICS_TABLE_ID = "player-table-statistics-body"
