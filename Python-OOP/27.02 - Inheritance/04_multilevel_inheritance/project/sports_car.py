from project.car import Car
from project.vehicle import Vehicle


class SportsCar(Car, Vehicle):
    def race(self):
        return "racing..."

