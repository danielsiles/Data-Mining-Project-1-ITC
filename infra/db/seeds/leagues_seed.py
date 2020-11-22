import json

from infra.db.connection import db_session
from domain.models.league import League


def leagues_seed():
    # Gets urls for popular leagues
    with open("popular_leagues.json", "r") as file:
        leagues = json.loads(file.read())
        for league in leagues:
            lg = League(**{"name": league["league_name"], "url": league["url"], "is_popular": True})
            db_session.merge(lg)
