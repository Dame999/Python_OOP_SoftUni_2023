from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[str] = []
        self.workers: List[str] = []

    def add_animal(self, animal, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salary = 0
        for worker in self.workers:
            workers_salary += worker.salary

        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost_to_care_for_animals = [a.money_for_care for a in self.animals]

        if self.__budget >= sum(total_cost_to_care_for_animals):
            self.__budget -= sum(total_cost_to_care_for_animals)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_count = len([a for a in self.animals if a.__class__.__name__ == "Lion"])
        tigers_count = len([a for a in self.animals if a.__class__.__name__ == "Tiger"])
        cheetahs_count = len([a for a in self.animals if a.__class__.__name__ == "Cheetah"])
        total_count_of_animals = lions_count + tigers_count + cheetahs_count

        lions = '\n'.join(a.__repr__() for a in self.animals if a.__class__.__name__ == "Lion")
        tigers = '\n'.join(a.__repr__() for a in self.animals if a.__class__.__name__ == "Tiger")
        cheetahs = '\n'.join(a.__repr__() for a in self.animals if a.__class__.__name__ == "Cheetah")

        return f"You have {total_count_of_animals} animals\n" \
               f"----- {lions_count} Lions:\n" + lions + "\n" \
               f"----- {tigers_count} Tigers:\n" + tigers + "\n" \
               f"----- {cheetahs_count} Cheetahs:\n" + cheetahs

    def workers_status(self):
        keepers_count = len([w for w in self.workers if w.__class__.__name__ == "Keeper"])
        caretakers_count = len([w for w in self.workers if w.__class__.__name__ == "Caretaker"])
        vets_count = len([w for w in self.workers if w.__class__.__name__ == "Vet"])
        total_workers_count = keepers_count + caretakers_count + vets_count

        keepers = '\n'.join(w.__repr__() for w in self.workers if w.__class__.__name__ == "Keeper")
        caretakers = '\n'.join(w.__repr__() for w in self.workers if w.__class__.__name__ == "Caretaker")
        vets = '\n'.join(w.__repr__() for w in self.workers if w.__class__.__name__ == "Vet")

        return f"You have {total_workers_count} workers\n" \
               f"----- {keepers_count} Keepers:\n" + keepers + "\n"\
               f"----- {caretakers_count} Caretakers:\n" + caretakers + "\n"\
               f"----- {vets_count} Vets:\n" + vets
