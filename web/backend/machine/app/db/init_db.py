from typing import List

from app import crud
from app.core import config
from app.models.user import UserCreate
from app.models.country import CountryCreate

# make sure all SQL Alchemy models are imported before initializing DB
# otherwise, SQL Alchemy might fail to initialize properly relationships
# for more details:
# https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
# from app.db import base


def add_superuser(db_session):
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db_session, email=config.FIRST_SUPERUSER)
    if not user:
        user_in = UserCreate(
            email=config.FIRST_SUPERUSER,
            password=config.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db_session, user_in=user_in)


def add_countries(db_session, countries: List[dict]):
    def add_country(country_in: dict):
        country = crud.country.get(db_session, country_id=country_in['id'])
        if not country:
            entry = CountryCreate(**country_in)
            country = crud.country.create(db_session, country_in=entry)

    list(map(add_country, countries))
