from bs4 import BeautifulSoup as bs


def get_league_fixtures(driver, url):
    driver.get(url)
    return driver.execute_script("return document.documentElement.outerHTML;")


def parse_league_fixtures(html):
    soup = bs(html, 'html.parser')
    table = soup.find(id="tournament-fixture")
    fixtures = table.find_all("div", class_="divtable-row")
    curr_date = ""
    matches = []
    for fixture in fixtures:
        header = fixture.find(class_="divtable-header")
        if header is not None:
            curr_date = header.get_text(" ", strip=True)
            continue

        match_time = fixture.find(class_="time").get_text(" ", strip=True)
        links = fixture.find_all("a")
        curr_link = "#"
        for link in links:
            if "Matches" in str(link) or "Live" in str(link):
                curr_link = link
        matches.append({
            "date": curr_date + " " + match_time,
            "result": curr_link.get_text(" ", strip=True),
            "url": curr_link["href"]
        })
    return matches