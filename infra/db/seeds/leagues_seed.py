import json

from domain.models.league import League
from infra.db.connection import DBConnection


def leagues_seed():
    """
    Reads the file popular_leagues.json that is the entry point of the program and updates the database.
    """
    with open("popular_leagues.json", "r") as file:
        leagues = json.loads(file.read())
        for league in leagues:
            lg = League(**{"name": league["league_name"], "url": league["url"], "is_popular": True})
            DBConnection.get_db_session().merge(lg)
            DBConnection.get_db_session().commit(lg)

