from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from datetime import datetime
from config.setup import engine


Base = declarative_base()


# declarative mapping
class Customer(Base):
    __tablename__ = "customers"

    # define the table columns
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    created_at = Column(DateTime(), default=datetime.now())


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
