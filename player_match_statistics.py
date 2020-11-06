from bs4 import BeautifulSoup as bs


def get_player_match_statistics_page_html(driver, url):
    driver.get(url)
    driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Offensive").click()
    driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Defensive").click()
    driver.find_element_by_id("live-player-home-options").find_element_by_link_text("Passing").click()
    driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Offensive").click()
    driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Defensive").click()
    driver.find_element_by_id("live-player-away-options").find_element_by_link_text("Passing").click()
    html = driver.execute_script("return document.documentElement.outerHTML;")
    return html



def parse_player_match_statistics(html):
    soup = bs(html, 'html.parser')
    home_players = []
    away_players = []
    types = ["home", "away"]
    team_ids = ["live-player-home-stats", "live-player-away-stats"]
    type_ids = ["summary", "offensive",
                "defensive", "passing"]
    for type in types:
        print(type)
        for type_id in type_ids:
            print(type_id)
            table = soup.find(id=f"live-player-{type}-stats").find(id=f"live-player-{type}-{type_id}").find(
                id="player-table-statistics-body")
            rows = table.find_all('tr')
            for index, row in enumerate(rows):
                cols = row.find_all('td')
                players = []
                for p_index, ele in enumerate(cols):
                    player_stat = ele.get_text(" ", strip=True)
                    if p_index == 0:
                        player_stat = ele.find("a").find("span").get_text(" ", strip=True)
                    if p_index == 1:
                        continue
                    players.append(player_stat)
                print(players)