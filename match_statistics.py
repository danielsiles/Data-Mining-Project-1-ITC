from bs4 import BeautifulSoup as bs


def get_match_statistics_page_html(driver, url):
    driver.get(url)
    element = driver.find_element_by_id('live-match').get_attribute('innerHTML')
    return element


def parse_match_statistics(html):
    soup = bs(html, 'html.parser')
    home_team = []
    away_team = []
    match_result = soup.find(id="match-centre-header").find(class_="score").get_text(" ", strip=True).split(":")
    home_team.append(match_result[0].replace(" ", ""))
    away_team.append(match_result[1].replace(" ", ""))
    match_statistics_table = soup.find(id="match-centre-stats").find("ul").find_all(class_="match-centre-stat")
    for row in match_statistics_table:
        stats = row.find_all("span", class_="match-centre-stat-value")
        home_team.append(stats[0].get_text(" ", strip=True))
        away_team.append(stats[1].get_text(" ", strip=True))
    row_keys = ["goals", "ratings", "shots", "possession", "pass_success", "dribles",
                "aerials_won", "tackles", "corners", "dispossessed"]

    print(dict(zip(row_keys, home_team)))
    print(dict(zip(row_keys, away_team)))