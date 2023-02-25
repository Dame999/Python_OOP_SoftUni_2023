class Vet:
    animals = []
    space = 5

    def __init__(self, name, animals=None):
        if animals is None:
            animals = []
        self.name = name
        self.animals = animals

    def register_animal(self, animal_name):
        if Vet.space > 0:
            Vet.space -= 1
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return f"Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            animal_to_remove = animal_name
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_to_remove} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animal. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
