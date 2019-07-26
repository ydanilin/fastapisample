from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class Country(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alpha_2 = Column(String)
    alpha_3 = Column(String)
    is_blacklisted = Column(Boolean(), default=False)
