import logging


from infra.parsers.base_parser import BaseParser
from bs4 import BeautifulSoup as bs

from config import MATCH_STATISTICS_RESULT_ID, MATCH_STATISTICS_SCORE_CLASS, MATCH_STATISTICS_TABLE_ID, \
    MATCH_STATISTICS_TABLE_ROW_CLASS, MATCH_STATISTICS_TABLE_ROW_VALUE_CLASS


logging.basicConfig(filename='match_statistics_parser_log_file.log',
                    format='%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s',
                    level=logging.INFO)


class MatchStatisticsParser(BaseParser):

    def parse(self, html):
        """
        Parse the html element that contains data about the match statistics
        :return: Statistics about the performance of each team in a match
        """
        soup = bs(html, 'html.parser')
        home_team = []
        away_team = []
        match_result = soup.find(id=MATCH_STATISTICS_RESULT_ID)\
            .find(class_=MATCH_STATISTICS_SCORE_CLASS).get_text(" ").split(":")
        home_team.append(match_result[0].replace(" ", ""))
        away_team.append(match_result[1].replace(" ", ""))
        match_statistics_table = soup.find(id=MATCH_STATISTICS_TABLE_ID).find("ul")\
            .find_all(class_=MATCH_STATISTICS_TABLE_ROW_CLASS)
        for row in match_statistics_table:
            logging.info(f"Parsing: {row}")
            stats = row.find_all("span", class_=MATCH_STATISTICS_TABLE_ROW_VALUE_CLASS)
            home_team.append(stats[0].get_text(" ", strip=True))
            away_team.append(stats[1].get_text(" ", strip=True))
        row_keys = ["goals", "ratings", "shots", "possession", "pass_success", "dribbles",
                    "aerials_won", "tackles", "corners", "dispossessed"]

        home_team = dict(zip(row_keys, home_team))
        away_team = dict(zip(row_keys, away_team))

        return home_team, away_team
