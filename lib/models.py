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
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())


if __name__ == "__main__":
    Base.metadata.create_all(engine)
