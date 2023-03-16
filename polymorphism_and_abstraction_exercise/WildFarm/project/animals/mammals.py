from abc import ABC

from project.animals.animal import Mammal
from project.animals.birds import Owl
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal, ABC):
    def make_sound(self):
        return "Squeak"

    @property
    def eatable_food(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal, ABC):
    def make_sound(self):
        return "Woof!"

    @property
    def gained_weight(self):
        return 0.40

    @property
    def eatable_food(self):
        return [Meat]


class Cat(Mammal, ABC):
    def make_sound(self):
        return "Meow"

    @property
    def eatable_food(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal, ABC):
    def make_sound(self):
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1.00

    @property
    def eatable_food(self):
        return [Meat]


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
