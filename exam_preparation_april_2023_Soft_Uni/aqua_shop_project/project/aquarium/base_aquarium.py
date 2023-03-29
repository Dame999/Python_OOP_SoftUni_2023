from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        sum_of_decorations_comfort = sum(d.comfort for d in self.decorations)
        return sum_of_decorations_comfort

    def add_fish(self, fish):
        fish_size_total = sum(f.size for f in self.fish)
        if fish_size_total > self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ == "FreshwaterFish" and self.__class__.__name__ == "FreshwaterAquarium":
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        elif fish.__class__.__name__ == "SaltwaterFish" and self.__class__.__name__ == "SaltwaterAquarium":
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def __str__(self):
        result = [f"{self.name}"]
        if self.fish:
            fish = ' '.join(f.name for f in self.fish)
            result.append(f"Fish: {fish}")
        else:
            result.append("Fish: none")

        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(result)

    def __check_aquarium_current_size(self):
        aquarium_size = sum(f.size for f in self.fish)
        return aquarium_size

    def feed(self):
        for fish in self.fish:
            fish.eat()

            if self.__check_aquarium_current_size() > self.capacity:
                fish.undo_eat()
                break

