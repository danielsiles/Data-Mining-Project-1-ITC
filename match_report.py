from bs4 import BeautifulSoup as bs


def get_match_report_page_html(driver, url):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML;")
    return html


def parse_match_report(html):
    soup = bs(html, 'html.parser')
    match_summary_table = soup.find("table", class_="matchstory")
    rows = match_summary_table.find_all('tr')

    home_summary = {"strengths": [], "weaknesses": [], "styles": []}
    away_summary = {"strengths": [], "weaknesses": [], "styles": []}
    types = ["strengths", "weaknesses", "styles"]
    type_id = -1
    for index, row in enumerate(rows):
        if index == 0:
            continue

        if row['class'][0] == "matchstory-typeheader":
            type_id += 1
            continue

        teams_data = row.find_all('td')
        home_data = teams_data[0].get_text(" ", strip=True)
        away_data = teams_data[1].get_text(" ", strip=True)
        if home_data != '':
            home_summary[types[type_id]].append(home_data)
        if away_data != '':
            away_summary[types[type_id]].append(away_data)

    print(home_summary)
    print(away_summary)