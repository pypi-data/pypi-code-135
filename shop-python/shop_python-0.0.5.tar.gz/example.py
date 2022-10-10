from dataclasses import dataclass
from shop_python.product.product import Product
from shop_python.pos.pos import POS
from shop_python.store import Store
from shop_python.customer.customer import Customer
import sys


def scenario():
    products = [
        Product(1, "Apple", 2.50, "Red Juicy Apple", 10),
        Product(2, "Banana", 3.50, "Yellow Bananas", 20),
        Product(3, "Carrot", 1.20, "Long carrots", 5),
    ]
    pos = POS(100.0)
    shop = Store("ABC Supermarket", products, pos)
    # shop.displayProducts()
    # shop.displayProduct("Apple")

    # Enter Bob
    bob = Customer("Bob", "20/09/1984", "bob@mailinator.com",
                   "+6732226111", "Somewhere in Brunei", [])


@dataclass
class Simulation:
    @staticmethod
    def intro():
        customer_name = input("What's your name?\n")
        customer_dob = input("What is your Date of Birth?\n")
        customer_email = input("What is your email?\n")
        customer_phone = input("What is your phone number?\n")
        customer_address = input("Where do you live?\n")
        customer = Customer(customer_name, customer_dob, customer_email,
                            customer_phone, customer_address, [])  # Handle KeyboardError
        print("Welcome to the shop!")
        print("We have the following goods:\n")
        products = [
            Product(1, "Apple", 2.50, "Red Juicy Apple", 10),
            Product(2, "Banana", 3.50, "Yellow Bananas", 20),
            Product(3, "Carrot", 1.20, "Long carrots", 5),
        ]
        pos = POS(100.0)
        shop = Store("Supermarket", products, pos)
        shop.displayProducts()
        Simulation.operations(customer, shop)

    @staticmethod
    def operations(customer, shop):
        print("What do you wanna do next?\n")
        customer_choice = input(
            "1. Check a Product\n2. Buy a Product\n3. Checkout\n")
        customer_choice = customer_choice.lower()
        if customer_choice in ['1', 'check', 'check a product', '1.']:
            shop.displayProducts()
            product = input("Sure! What product do you want to check?\n")
            customer.checkProduct(product, shop)
            Simulation.operations(customer, shop)
        if customer_choice in ['2', 'buy', 'buy a product', '2.']:
            shop.displayProducts()
            product = input("Sure! What product do you want to buy?\n")
            selected = shop.displayProduct(product)
            customer.buy(selected)
            Simulation.operations(customer, shop)
        if customer_choice in ['3', 'checkout', '3.']:
            raise NotImplementedError
            shop.checkout()
            continue_shop = input("Do you want to continue shopping? (Y/N)\n")
            if continue_shop.upper() in ('Y', 'YE', 'YES'):
                Simulation.operations(customer, shop)
            else:
                sys.exit()


if __name__ == "__main__":
    try:
        Simulation.intro()
    except KeyboardInterrupt:
        exit_shop = input(
            "CTRL + C detected. Did you mean to quit the shop simulator? (Y/N)\n")
        if exit_shop in ('Y', 'YE', 'YES', 'OK', 'BET', 'ALRIGHT'):
            print("Alright! Thank you for shopping at this simulated shop! Bye Bye!")
            import sys
            sys.exit()
