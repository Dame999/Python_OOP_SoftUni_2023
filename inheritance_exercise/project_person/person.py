class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Child(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
