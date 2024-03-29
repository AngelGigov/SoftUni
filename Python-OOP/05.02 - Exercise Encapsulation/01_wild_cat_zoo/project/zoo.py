from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name:str, budget:int, animal_capacity:int, workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= len(self.workers):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.workers.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money = sum([a.money_for_care for a in self.workers])
        if self.__budget < total_money:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.workers:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(repr(animal))

        result = [f"You have {len(self.workers)} animals", f"----- {len(lions)} Lions:"]
        result.extend(lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(repr(worker))
            elif worker.__class__.__name__ == "Vet":
                vets.append(repr(worker))

        result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        result.extend(keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(result)

    # def add_animal(self, animal: Animal, price):
    #     if self.__budget < price:
    #         return "Not enough budget"
    #     elif self.__animal_capacity < 1:
    #         return "Not enough space for animal"
    #     self.animals.append(animal)
    #     self.__animal_capacity -= 1
    #     self.__budget -= price
    #     return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
    #
    # def hire_worker(self, worker: Worker):
    #     if self.__workers_capacity < 1:
    #         return "Not enough space for worker"
    #     self.workers.append(worker)
    #     self.__workers_capacity -= 1
    #     return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    #
    # def fire_worker(self, worker_name):
    #     try:
    #         worker = next(filter(lambda w: w.name == worker_name , self.workers))
    #     except StopIteration:
    #         return f"There is no {worker_name} in the zoo"
    #
    #     self.workers.remove(worker)
    #     return f"{worker_name} fired successfully"
    #
    # def pay_workers(self): # salary_sum can keep the amount forever (be aware to clear it)
    #     salary_sum = 0
    #     for worker in self.workers:
    #         salary_sum += worker.salary
    #     if self.__budget < salary_sum:
    #         salary_sum = 0
    #         return "You have no budget to pay your workers. They are unhappy"
    #     self.__budget -= salary_sum
    #     salary_sum = 0
    #     return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    #
    # def tend_animals(self):
    #     total_money_for_care = 0
    #     for animal in self.animals:
    #         total_money_for_care += animal.money_for_care
    #     if self.__budget < total_money_for_care:
    #         total_money_for_care = 0
    #         return "You have no budget to tend the animals. They are unhappy."
    #     self.__budget -= total_money_for_care
    #     total_money_for_care = 0
    #     return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    #
    # def profit(self, amount:int):
    #     self.__budget += amount
    #
    # def animals_status(self):
    #     total_animals_count = len(self.animals)
    #     animal_groups = {}
    #
    #     # Group animals by their class (Lion, Tiger, Cheetah)
    #     for animal in self.animals:
    #         animal_class = animal.__class__.__name__
    #         if animal_class not in animal_groups:
    #             animal_groups[animal_class] = []
    #
    #         animal_info = f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}"
    #         animal_groups[animal_class].append(animal_info)
    #
    #     # Construct the result string
    #     result = f"You have {total_animals_count} animals\n"
    #     for animal_class, animal_list in animal_groups.items():
    #         result += f"----- {len(animal_list)} {animal_class}s:\n"
    #         result += '\n'.join(animal_list) + '\n'
    #
    #     return result.strip()
    #
    # def workers_status(self):
    #     total_workers_count = len(self.workers)
    #     keepers = []
    #     caretakers = []
    #     vets = []
    #
    #     for worker in self.workers:
    #         if isinstance(worker, Keeper):
    #             keepers.append(f"Name: {worker.name}, Age: {worker.age}, Salary: {worker.salary}")
    #         elif isinstance(worker, Caretaker):
    #             caretakers.append(f"Name: {worker.name}, Age: {worker.age}, Salary: {worker.salary}")
    #         elif isinstance(worker, Vet):
    #             vets.append(f"Name: {worker.name}, Age: {worker.age}, Salary: {worker.salary}")
    #
    #     result = f"You have {total_workers_count} workers\n"
    #     result += f"----- {len(keepers)} Keepers:\n"
    #     result += '\n'.join(keepers) + '\n'
    #
    #     result += f"----- {len(caretakers)} Caretakers:\n"
    #     result += '\n'.join(caretakers) + '\n'
    #
    #     result += f"----- {len(vets)} Vets:\n"
    #     result += '\n'.join(vets) + '\n'
    #
    #     return result.strip()
