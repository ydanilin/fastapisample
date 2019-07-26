import logging
import json

from app.db.init_db import add_superuser, add_countries
from app.db.session import db_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init():
    add_superuser(db_session)
    # world.json obtained from here:
    # http://stefangabos.github.io/world_countries/
    f = open("world.json", "r")
    countries = json.load(f)
    add_countries(db_session, countries)
    f.close()


def main():
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
