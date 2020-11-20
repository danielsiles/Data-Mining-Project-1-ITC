from infra.parsers.base_parser import BaseParser
from bs4 import BeautifulSoup as bs

from config import FIXTURE_TABLE_ID, FIXTURE_TABLE_ROW, FIXTURE_TABLE_HEADER


class MatchParser(BaseParser):

    def __init__(self, html):
        super().__init__(html)

    def parse(self):
        """
        Parse the html element that contains data about league fixtures
        :return: The list of matches played or to be played with the date, result and url for details
        """
        soup = bs(self._html, 'html.parser')
        table = soup.find(id=FIXTURE_TABLE_ID)
        fixtures = table.find_all("div", class_=FIXTURE_TABLE_ROW)
        curr_date = ""
        matches = []
        for fixture in fixtures:
            header = fixture.find(class_=FIXTURE_TABLE_HEADER)
            if header is not None:
                curr_date = header.get_text(" ", strip=True)
                continue

            match_time = fixture.find(class_="time").get_text(" ", strip=True)
            links = fixture.find_all("a")
            curr_link = {"href": "#"}
            for link in links:
                if "Matches" in str(link) or "Live" in str(link):
                    curr_link = link
            matches.append({
                "date": curr_date + " " + match_time,
                "result": curr_link.get_text(" ", strip=True),
                "url": curr_link['href']
            })
        return matches

