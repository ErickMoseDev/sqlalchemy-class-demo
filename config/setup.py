from sqlalchemy import create_engine


# create database connection
db_url = "sqlite:///db/store.db"

engine = create_engine(db_url, echo=False)


# with engine.connect() as connection:
#     pass
