from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base

from datetime import datetime


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
meta = MetaData(naming_convention=convention)

Base = declarative_base(metadata=meta)


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
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_id = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False, default="pending")
    order_date = Column(DateTime(), default=datetime.now())
    total_amount = Column(Float, nullable=False)

    # foreign key (many side of the relationship)
    customer_id = Column(Integer, ForeignKey("customers.id"))


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)

    # add foreign keys
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    # relationships


# relationship between a customer and an order
# 1 to many
