from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            self.decorations_repository.decorations.append(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.decorations.append(Plant())

        return f"Successfully added {decoration_type}."

    def __decoration_finder(self, decoration_type: str):
        for d in self.decorations_repository.decorations:
            if d.__class__.__name__ == decoration_type:
                return d

    def __aquarium_finder(self, aquarium_name: str):
        for a in self.aquariums:
            if a.name == aquarium_name:
                return a

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.__decoration_finder(decoration_type)
        aquarium = self.__aquarium_finder(aquarium_name)

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        elif aquarium and decoration:
            aquarium.decorations.append(decoration)
            self.decorations_repository.decorations.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__aquarium_finder(aquarium_name)

        if fish_type == "FreshwaterFish" and aquarium:
            return aquarium.add_fish(FreshwaterFish(fish_name, fish_species, price))
        elif fish_type == "SaltwaterFish" and aquarium:
            return aquarium.add_fish(SaltwaterFish(fish_name, fish_species, price))

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__aquarium_finder(aquarium_name)

        if aquarium:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    @staticmethod
    def __calculate_total_fish_price(aquarium: BaseAquarium):
        total_price = sum(f.price for f in aquarium.fish)
        return total_price

    @staticmethod
    def __calculate_total_decoration_price(aquarium: BaseAquarium):
        total_price = sum(d.price for d in aquarium.decorations)
        return total_price

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__aquarium_finder(aquarium_name)

        if aquarium:
            total_sum = self.__calculate_total_fish_price(aquarium) + self.__calculate_total_fish_price(aquarium)
            return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return '\n'.join(result)
