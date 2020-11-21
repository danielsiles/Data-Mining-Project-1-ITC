from infra.parsers.base_parser import BaseParser
from bs4 import BeautifulSoup as bs

from config import MATCH_REPORT_SUMMARY_TABLE_CLASS, MATCH_REPORT_SUMMARY_TABLE_HEADER_CLASS


class MatchReportParser(BaseParser):

    def parse(self, html):
        """
        Parse the html element that contains data about the match report
        :return: The list of strengths, weaknesses and styles for each team in the match
        """
        soup = bs(html, 'html.parser')
        match_summary_table = soup.find("table", class_=MATCH_REPORT_SUMMARY_TABLE_CLASS)
        rows = match_summary_table.find_all('tr')

        home_summary = {"strengths": [], "weaknesses": [], "styles": []}
        away_summary = {"strengths": [], "weaknesses": [], "styles": []}
        types = ["strengths", "weaknesses", "styles"]
        type_id = -1
        for index, row in enumerate(rows):
            if index == 0:
                continue

            if row['class'][0] == MATCH_REPORT_SUMMARY_TABLE_HEADER_CLASS:
                type_id += 1
                continue

            teams_data = row.find_all('td')
            home_data = teams_data[0].get_text(" ", strip=True)
            away_data = teams_data[1].get_text(" ", strip=True)
            if home_data != '':
                home_summary[types[type_id]].append(home_data)
            if away_data != '':
                away_summary[types[type_id]].append(away_data)

        return home_summary, away_summary
