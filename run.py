#!/usr/bin/env python3

from config.setup import engine

from lib.models import Customer, Product


def add_customers():
    pass


def fetch_all_customers():
    pass


def fetch_one_customer():
    pass


# simple cli to insert data
def main():
    cli_actions = {
        "1": add_customers,
        "2": fetch_all_customers,
        "3": fetch_one_customer,
    }

    while True:
        print("Select an option below:")
        print("1. Add customers")
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


if __name__ == "__main__":
    main()
