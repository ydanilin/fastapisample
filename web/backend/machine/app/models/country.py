from typing import Optional

from pydantic import BaseModel, Schema


class CountryBase(BaseModel):
    id: Optional[int] = 0
    name: Optional[str] = None
    alpha2: Optional[str] = None
    alpha3: Optional[str] = None
    is_blacklisted: Optional[bool] = False


class CountryCreate(CountryBase):
    id: int
    name: str
    alpha2: str
    alpha3: str


class CountryOut(BaseModel):
    id: int = Schema(
        ...,
        alias="numeric_code",
        title="Country numeric code",
        description="ISO 3166-1"
    )
    name: str = Schema(
        ...,
        alias="country_name",
        title="Country name",
        description="Usual name"
    )
    alpha_2: str = Schema(
        ...,
        alias="word_code",
        title="Two-letter code",
        description="Per ISO 3166-1 alpha-2 format"
    )

    class Config:
        title = "Country Record"
        orm_mode = True
        allow_population_by_alias = True


# class CountryOutA(BaseModel):
#     numeric_code: int = Schema(..., title="Numeric code", alias="id")
#     country_name: str = Schema(..., title="Usual name", alias="name")
#     word_code: str = Schema(..., title="Two-letter code", alias="alpha_2")

#     class Config:
#         orm_mode = True
