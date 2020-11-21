from infra.parsers.base_parser import BaseParser
from bs4 import BeautifulSoup as bs

from config import FIXTURE_TABLE_ID, FIXTURE_TABLE_ROW, FIXTURE_TABLE_HEADER


class MatchParser(BaseParser):

    def parse(self, html):
        """
        Parse the html element that contains data about league fixtures
        :return: The list of matches played or to be played with the date, result and url for details
        """
        soup = bs(html, 'html.parser')
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
            curr_link = fixture.find("div", class_="result").find("a")
            result = curr_link.get_text(" ", strip=True).split(" : ")
            home_goals = None
            away_goals = None
            if len(result) > 1:
                home_goals = result[0]
                away_goals = result[1]

            team_links = fixture.find_all("a", class_="team-link")
            matches.append({
                "date": curr_date + " " + match_time,
                "home_goals": home_goals,
                "away_goals": away_goals,
                "home_team": team_links[0].get_text(" ", strip=True),
                "home_team_url": team_links[0]["href"],
                "away_team": team_links[1].get_text(" ", strip=True),
                "away_team_url": team_links[1]["href"],
                "url": curr_link['href']
            })
        return matches

