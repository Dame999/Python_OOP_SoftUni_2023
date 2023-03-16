from project.cat import Cat
from project.dog import Dog


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return "Hiss"

