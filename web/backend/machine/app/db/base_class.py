from sqlalchemy.ext.declarative import declarative_base, declared_attr


class CustomBase(object):
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        cname = cls.__name__.lower()
        base, suffix = (
            (cname, "s") if cname[-1] != "y" else (cname[:-1], "ies")
        )
        return f"{base}{suffix}"


Base = declarative_base(cls=CustomBase)
