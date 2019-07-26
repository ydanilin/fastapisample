from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Path

from app.api.utils.db import get_db
from app.models.country import CountryOut
from app import crud


router = APIRouter()


@router.get(
    "/{country_name}",
    response_model=CountryOut,
    summary="Informs whether country is blacklisted",
    response_description="Country details"
)
def is_country_blacklisted(
    country_name: str = Path(
        ...,
        description="Usual name",
        example="Burkina Faso",
    ),
    db: Session = Depends(get_db)
):
    """
    Some countries may be **blacklisted** due to the following reasons:

    - they have **Putin**
    - they have Somali pirates
    - other reasons as decided by the Zionist Occupational Government
    """
    country = crud.country.get_by_name(
        db_session=db, country_name=country_name
    )
    return country
