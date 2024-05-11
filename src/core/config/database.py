from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "{engine}://{user}:{password}@{host}:{port}/{database}".format(
        engine="postgresql",
        user=config("DB_USER"),
        password=config("DB_PASSWORD"),
        host=config("DB_HOST"),
        port=config("DB_PORT"),
        database=config("DB_NAME"),
    )
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


def get_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
