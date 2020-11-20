import json

from main.factories.parser.parser_factory import make_league_table_parser

from main.factories.scraper.scraper_factory import make_league_table_scraper


def get_popular_leagues():
    # Gets urls for popular leagues
    with open("popular_leagues.json", "r") as file:
        return json.loads(file.read())


def pretty_print(elem):
    """
    Formats the dictionary and print it to the console.
    :param elem: Dictionary to be printed
    """
    print(json.dumps(elem, indent=4, sort_keys=True))


def main():
    """
    Main function. Execute all the test scripts to scrape the data.
    """
    league = get_popular_leagues()[0]
    pretty_print(make_league_table_parser(make_league_table_scraper(league['url']).scrape()).parse())
    # league_table_html = get_league_page_html(driver, BASE_URL + league['url'])
    # league_table = parse_league_table_data(league_table_html)
    #
    # pretty_print(league_table)
    #
    # league_fixtures_html = get_league_fixtures(driver, BASE_URL + league['url'].replace("Show", "Fixtures"))
    # league_fixtures = parse_league_fixtures(league_fixtures_html)
    #
    # pretty_print(league_fixtures)
    #
    # match_statistics_html = get_match_statistics_page_html(driver,
    #                                                        BASE_URL + league_fixtures[0]["url"].replace("Show", "Live"))
    # match_statistics_home, match_statistics_away = parse_match_statistics(match_statistics_html)
    #
    # pretty_print(match_statistics_home)
    # pretty_print(match_statistics_away)
    #
    # match_report_html = get_match_report_page_html(driver,
    #                                                BASE_URL + league_fixtures[0]["url"].replace("Show", "MatchReport"))
    # match_report_home, match_report_away = parse_match_report(match_report_html)
    #
    # pretty_print(match_report_home)
    # pretty_print(match_report_away)
    #
    # player_match_statistics_html = get_player_match_statistics_page_html(driver,
    #                                                                      BASE_URL + league_fixtures[0]["url"].replace(
    #                                                                          "Show", "LiveStatistics"))
    # player_match_statistics = parse_player_match_statistics(player_match_statistics_html)
    #
    # pretty_print(player_match_statistics)


if __name__ == '__main__':
    main()
