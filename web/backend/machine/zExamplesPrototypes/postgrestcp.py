from sqlalchemy import create_engine
from app.core import config


print(config.SQLALCHEMY_DATABASE_URI)
engine = create_engine(
    # 'postgres://test:shalom@localhost:5432/example'
    config.SQLALCHEMY_DATABASE_URI
    # 'postgres://test:shalom@/example?host=/var/uvicorn_sockdir'
)
engine.connect()
