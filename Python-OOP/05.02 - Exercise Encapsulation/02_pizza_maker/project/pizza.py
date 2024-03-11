from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 1:
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        else:
            self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if self.max_number_of_toppings <= len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight
    def calculate_total_weight(self):
        pizza_total_weight = self.dough.weight + sum(self.toppings.values())
        return pizza_total_weight
