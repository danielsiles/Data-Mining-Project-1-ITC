from infra.parsers.base_parser import BaseParser
from bs4 import BeautifulSoup as bs

from config import MATCH_STATISTICS_RESULT_ID, MATCH_STATISTICS_SCORE_CLASS, MATCH_STATISTICS_TABLE_ID, \
    MATCH_STATISTICS_TABLE_ROW_CLASS, MATCH_STATISTICS_TABLE_ROW_VALUE_CLASS, PLAYER_STATISTICS_TABLE_ID


class MatchPlayerStatisticsParser(BaseParser):

    def parse(self, html):
        """
        Parse the html element that contains data about the players in a match
        :return: Statistics about all the players of a match
        """
        soup = bs(html, 'html.parser')
        home_players = {}
        away_players = {}

        types = ["home", "away"]
        type_ids = ["summary", "offensive",
                    "defensive", "passing"]

        summary_keys = ["player_name", "shots", "shots_on_target", "key_passes", "pass_success", "aerials_won",
                        "touches",
                        "rating"]
        offensive_keys = ["player_name", "shots", "shots_on_target", "key_passes", "dribbles_won", "fouls_given",
                          "offside_given", "dispossessed", "turnover", "rating"]
        defensive_keys = ["player_name", "tackles", "interceptions", "clearances", "shots_blocked", "fouls_committed",
                          "rating"]
        passing_keys = ["player_name", "key_passes", "passes", "pass_success", "crosses", "cross_success", "long_ball",
                        "long_ball_success", "through_ball", "through_ball_success"]

        data = {"home": home_players, "away": away_players}
        keys = dict(zip(type_ids, [summary_keys, offensive_keys, defensive_keys, passing_keys]))
        for tp in types:
            for type_id in type_ids:
                table = soup.find(id=f"live-player-{tp}-stats").find(id=f"live-player-{tp}-{type_id}").find(
                    id=PLAYER_STATISTICS_TABLE_ID)
                rows = table.find_all('tr')
                for index, row in enumerate(rows):
                    cols = row.find_all('td')
                    players = []
                    for p_index, ele in enumerate(cols):
                        player_stat = ele.get_text(" ", strip=True)
                        if p_index == 0:
                            player_number = ele.find("a").find("div").get_text(" ", strip=True)
                            players.append(player_number)
                            player_stat = ele.find("a").find("span").get_text(" ", strip=True)
                        if p_index == 1:
                            continue
                        players.append(player_stat)

                    if players[0] not in data[tp]:
                        data[tp][players[0]] = {}
                    else:
                        data[tp][players[0]].update(dict(zip(keys[type_id], players[1:])))

                    print(data)

        return data
