from abc import ABC

from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird, ABC):
    def make_sound(self):
        return "Hoot Hoot"

    @property
    def eatable_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird, ABC):
    def make_sound(self):
        return "Cluck"

    @property
    def eatable_food(self):
        return [Meat, Vegetable, Seed, Fruit]

    @property
    def gained_weight(self):
        return 0.35



