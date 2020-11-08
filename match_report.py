from bs4 import BeautifulSoup as bs


def get_match_report_page_html(driver, url):
    """
    Get the html page with the report of a match
    :param driver: driver to navigate to url and execute script
    :param url: A url of the website that will be scraped by the driver
    :return: Html element scraped by the driver
    """
    driver.get(url)
    return driver.execute_script("return document.documentElement.outerHTML;")


def parse_match_report(html):
    """
    Parse the html element that contains data about the match report
    :param html: Html element scraped to be parsed
    :return: The list of strengths, weaknesses and styles for each team in the match
    """
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

    return home_summary, away_summary
