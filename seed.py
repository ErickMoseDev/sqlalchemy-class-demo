# seeding dummy data
# faker

from lib.models import Customer, Product, Order, OrderItem
from config.setup import Session

# add a session instance
session = Session()

# remove any previous seed data
print("Removing previous seed data... 🌱")
session.query(Customer).delete()
session.query(Product).delete()
session.query(Order).delete()
session.query(OrderItem).delete()


# add customers
customer1 = Customer(
    first_name="Jane",
    last_name="Doe",
    email="janedoe@gmail.com",
    phone="0786543218",
    gender="Female",
    age=27,
)
customer2 = Customer(
    first_name="Johnny",
    last_name="Boy",
    email="johnnyboy@gmail.com",
    phone="0712345678",
    gender="Male",
    age=30,
)
customer3 = Customer(
    first_name="Hope",
    last_name="Yunia",
    email="hope@gmail.com",
    phone="0712389745",
    gender="Female",
    age=24,
)
customer4 = Customer(
    first_name="Masela",
    last_name="Ogendo",
    email="masela@gmail.com",
    phone="0712354321",
    gender="Female",
    age=25,
)
customer5 = Customer(
    first_name="Eugene",
    last_name="Wekesa",
    email="eugene@gmail.com",
    phone="0743529875",
    gender="Male",
    age=45,
)


product1 = Product(
    name="Wireless Mouse",
    description="Ergonomic wireless mouse with adjustable DPI.",
    category="Electronics",
    price=29.99,
    rating=4.5,
    quantity=100,
)
product2 = Product(
    name="Yoga Mat",
    description="Non-slip yoga mat suitable for all levels.",
    category="Fitness",
    price=19.99,
    rating=4.2,
    quantity=50,
)
product3 = Product(
    name="Coffee Maker",
    description="12-cup programmable coffee maker with auto shut-off.",
    category="Home Appliances",
    price=49.99,
    rating=4.7,
    quantity=30,
)
product4 = Product(
    name="Bluetooth Headphones",
    description="Over-ear headphones with noise cancellation.",
    category="Audio",
    price=89.99,
    rating=4.3,
    quantity=75,
)
product5 = Product(
    name="Sketchbook",
    description="A4-sized sketchbook with 100 acid-free pages.",
    category="Art Supplies",
    price=12.49,
    rating=4.6,
    quantity=200,
)

order1 = Order(
    order_id="ORNo-123", status="pending", total_amount=300, customer=customer1
)
order2 = Order(order_id="ORNo-124", status="delivered", total_amount=800)
order3 = Order(order_id="ORNo-125", status="pending", total_amount=7000)
order4 = Order(order_id="ORNo-126", status="in transit", total_amount=8000)
order5 = Order(order_id="ORNo-127", status="delivered", total_amount=100)

# associate orders with customers
# customer1.orders.append(order1)
customer1.orders.append(order4)
customer2.orders.append(order2)
customer3.orders.append(order3)
# customer4.orders.append(order5)

# technique 2
order5.customer = customer4

# technique 3


# associate order items with orders
order_item1 = OrderItem(quantity=5, product=product2, order=order2)
order_item2 = OrderItem(quantity=1, product=product1, order=order1)
order_item3 = OrderItem(quantity=3, product=product3, order=order4)
order_item4 = OrderItem(quantity=7, product=product1, order=order1)
order_item5 = OrderItem(quantity=2, product=product4, order=order5)
order_item6 = OrderItem(quantity=2, product=product5, order=order3)

session.add_all(
    [
        customer1,
        customer2,
        customer3,
        customer4,
        customer5,
        product1,
        product2,
        product3,
        product4,
        product5,
        order1,
        order2,
        order3,
        order4,
        order5,
        order_item1,
        order_item2,
        order_item3,
        order_item4,
        order_item5,
        order_item6,
    ]
)
session.commit()

print("Finished adding seed data... 🌱")
