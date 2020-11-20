from bs4 import BeautifulSoup as bs

from config import LEAGUE_TABLE_CLASS


def get_league_page_html(driver, url):
    """
    Get the html page of a league with information about table
    :param driver: driver to navigate to url and execute script
    :param url: A url of the website that will be scraped by the driver
    :return: Html element scraped by the driver
    """
    driver.get(url)
    return driver.execute_script("return document.documentElement.outerHTML;")


def parse_league_table_data(html):
    """
    Parse the html element that contains data about league table
    :param html: Html element scraped to be parsed
    :return: The list of teams of a league with all the data with respect to the performance at the league
    """
    # soup = bs(html, 'html.parser')
    # tournament_table = soup.find("div", class_=LEAGUE_TABLE_CLASS)
    # league_table_rows = tournament_table.find("tbody", class_=LEAGUE_TABLE_ROW_CLASS)
    # tr = []
    # for league_table_row in league_table_rows:
    #     team_infos = league_table_row.find_all('td')
    #     tr_info = []
    #     team_name = team_infos[0]
    #     tr_info.append(team_name.a.text)
    #     tr_info.append(team_name.a["href"])
    #     for team_info in team_infos[1:]:
    #         tr_info.append(team_info.text)
    #     row_keys = ["team_name", "team_url", "matches_played", "win",
    #                 "draw", "loss", "goal_for", "goal_against",
    #                 "goal_difference", "points"" form"
    #                 ]
    #
    #     tr.append(dict(zip(row_keys, tr_info)))
    #
    # return tr
