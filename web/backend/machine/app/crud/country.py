from typing import Optional
from sqlalchemy.orm import Session

from app.db_models.country import Country
from app.models.country import CountryCreate


def create(db_session: Session, *, country_in: CountryCreate) -> Country:
    country = Country(
        id=country_in.id,
        name=country_in.name,
        alpha_2=country_in.alpha2,
        alpha_3=country_in.alpha3,
    )
    db_session.add(country)
    db_session.commit()
    return country


def get_by_name(
    db_session: Session, *, country_name: str
) -> Optional[Country]:
    return db_session.query(
        Country).filter(Country.name.ilike(country_name)).first()
