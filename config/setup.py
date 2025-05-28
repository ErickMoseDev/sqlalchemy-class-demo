from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# create database connection
db_url = "sqlite:///db/store.db"

engine = create_engine(db_url, echo=False)


# create a Session class
Session = sessionmaker(bind=engine)
