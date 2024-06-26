from abc import ABC, abstractmethod
from typing import List
from project.equipment.base_equipment import BaseEquipment
from math import floor


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float) -> object:
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = sum([e.price for e in self.equipment])
        avg_team_protection = sum([e.protection for e in self.equipment]) / len(self.equipment)

        result = f"Name: {self.name}\n"
        result += f"Country: {self.country}\n"
        result += f"Advantage: {self.advantage} points\n"
        result += f"Budget: {self.budget:.2f}EUR\n"
        result += f"Wins: {self.wins}\n"
        result += f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n"
        result += f"Average Protection: {floor(avg_team_protection)}"

        return result
