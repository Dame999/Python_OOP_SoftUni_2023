class Customer:
    def __init__(self, name: str, age: int, id_num: int):
        self.name = name
        self.age = age
        self.id = id_num
        self.rented_dvds = []

    def __repr__(self):
        dvd_names = ', '.join(i.name for i in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented " \
               f"DVD's ({dvd_names})"
