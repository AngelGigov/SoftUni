from project.product import Product


class Drink(Product):
    # DEFAULT_QUANTITY = 15

    def __init__(self, name: str):
        super().__init__(name, quantity=10)