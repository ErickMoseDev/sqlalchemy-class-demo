#!/usr/bin/env python3

from config.setup import Session
from lib.models import Customer


# session instance
session = Session()


def printMessage(message):
    print(
        f"-----------------------------------------------\n{message}\n------------------------------------------------"
    )


def add_customers():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    email = input("Enter the customer email: ")
    phone = input("Enter the customer phone: ")
    gender = input("Enter the customers gender: ")

    while True:
        age = input("Enter the customers age: ")

        if not age.isdigit():
            print("Age has to be a number. Please try again!")
            continue

        try:
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                gender=gender,
                age=int(age),
            )

            session.add(customer)
            session.commit()

            printMessage("Customer added Successfully!")
            return

        except Exception as e:
            print(f"An Error occured: {e}")
            session.rollback()


def fetch_all_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print("------------------------------------------------------")
        print(f"id: {customer.id}")
        print(f"firstname: {customer.first_name}")
        print(f"lastname: {customer.last_name}")
        print(f"email: {customer.email}")
        print(f"phone: {customer.phone}")
        print(f"gender: {customer.gender}")
        print(f"age: {customer.age}")
        print("------------------------------------------------------")


def fetch_one_customer():
    customer_id = input("Enter a customer id: ")

    try:
        customer = session.query(Customer).filter_by(id=customer_id).one_or_none()

        orders = customer.orders

        print(
            f"Here are your associated orders Mr/Mrs {customer.first_name} {customer.last_name}"
        )

        for order in orders:
            print("------------------------------------------------------")
            print(f"order_id: {order.order_id}")
            print(f"status: {order.status}")
            print(f"total: {order.total_amount}")
            print("The following are the order items:")
            for item in order.order_items:
                print(f"product name: {item.product.name}")
                print(f"product category: {item.product.category}")
                print(f"product price: {item.product.price}")
                print(f"product quantity: {item.quantity}")
                print("------------------------------------------------------")

    except Exception as e:
        print(f"Error occured: {e}")
        session.rollback()


def update_customer():
    while True:
        customer_id = input("Enter the customer id: ")

        if not customer_id.isdigit():
            print("Customer id has to be a digit. Try again!")
            continue

        try:
            customer = session.query(Customer).filter_by(id=customer_id).one_or_none()

            if customer:
                fname = input("Enter the updated first name: ")
                lname = input("Enter the updated last name: ")
                email = input("Enter the updated email: ")
                phone = input("Enter the updated phone number: ")
                gender = input("Enter the updated gender: ")
                age = input("Enter the updated age: ")

                # update the db with the latest changes
                customer.first_name = fname or customer.first_name
                customer.last_name = lname or customer.last_name
                customer.email = email or customer.email
                customer.phone = phone or customer.phone
                customer.gender = gender or customer.gender
                customer.age = age or customer.age

                session.commit()
                printMessage("User updated successfully!")
                return
            else:
                printMessage("Invalid Customer id. Try again!")

        except Exception as e:
            print(f"Error occured: {e}")
            session.rollback()


# simple cli to insert data
def main():
    cli_actions = {
        "1": add_customers,
        "2": fetch_all_customers,
        "3": fetch_one_customer,
        "7": update_customer,
    }

    print(
        "-------------------------------------------------------------\nWELCOME TO THE INVICTUS SHOP.\nWE SELL KNOWLEDGE.\nTAP INTO THE MYSTERIES OF YOUR BRAIN AND UNLOCK NEW HORIZONS\n-------------------------------------------------------------"
    )

    while True:
        print("Select an option below:")
        print("1. Add a customer")
        print("2. Fetch all customers")
        print("3. Fetch one customer")
        print("4. Add a product")
        print("5. Fetch one product")
        print("6. Fetch all products")
        print("7. Update one customer")
        print("8. Update one product")
        print("9. Delete one customer")
        print("10.Delete one product")
        print("0. Exit")

        choice = input("Enter an option: ")

        if choice == "0":
            print(
                "-----------------------------------------------\nThank you for visiting our store. Welcome again!\n------------------------------------------------"
            )
            break

        action = cli_actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice! Try again")
            print("*************************************************************")


if __name__ == "__main__":
    main()
