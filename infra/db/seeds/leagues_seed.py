import json

from sqlalchemy.exc import IntegrityError

from domain.models.league import League
from infra.db.connection import DBConnection
from main.factories.use_cases.use_cases_factory import make_scrape_league_matches_use_case, \
    make_scrape_league_table_use_case


def leagues_seed(populate=False):
    # Gets urls for popular leagues
    with open("popular_leagues.json", "r") as file:
        leagues = json.loads(file.read())
        for league in leagues:
            lg = League(**{"name": league["league_name"], "url": league["url"],
                           "odds_api_league_key": league["odds_api_league_key"],
                           "fixture_url": league["fixture"], "is_popular": True})
            try:
                DBConnection.get_db_session().merge(lg)
                DBConnection.get_db_session().commit()
            except IntegrityError:
                DBConnection.get_db_session().rollback()
                print("Leagues already exists in the DB")

            if populate:
                make_scrape_league_table_use_case(league["league_name"]).execute()
                make_scrape_league_matches_use_case(league["league_name"]).execute()
