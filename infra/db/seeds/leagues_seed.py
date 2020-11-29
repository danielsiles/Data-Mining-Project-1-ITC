import json

from sqlalchemy.exc import IntegrityError

from domain.models.league import League
from infra.db.connection import DBConnection


def leagues_seed():
    # Gets urls for popular leagues
    with open("popular_leagues.json", "r") as file:
        leagues = json.loads(file.read())
        for league in leagues:
            lg = League(**{"name": league["league_name"], "url": league["url"], "is_popular": True})
            try:
                DBConnection.get_db_session().merge(lg)
                DBConnection.get_db_session().commit()
            except IntegrityError:
                DBConnection.get_db_session().rollback()
                print("Leagues already exists in the DB")
