from bs4 import BeautifulSoup as bs


def get_league_page_html(driver, url):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    return html


def parse_league_table_data(html):
    soup = bs(html, 'html.parser')
    tournament_table = soup.find("div", class_="tournament-standings-table")
    league_table_rows = tournament_table.find("tbody", class_="standings")
    tr = []
    for league_table_row in league_table_rows:
        team_infos = league_table_row.find_all('td')
        tr_info = []
        team_name = team_infos[0]
        tr_info.append(team_name.a.text)
        tr_info.append(team_name.a["href"])
        for team_info in team_infos[1:]:
            tr_info.append(team_info.text)
        row_keys = ["team_name", "team_url", "matches_played", "win",
                    "draw", "loss", "goal_for", "goal_against",
                    "goal_difference", "points"" form"
                    ]

        tr.append(dict(zip(row_keys, tr_info)))

    return tr