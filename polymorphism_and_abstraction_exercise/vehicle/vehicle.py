from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    AIR_CONDITIONER_ON = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + Car.AIR_CONDITIONER_ON) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Car.AIR_CONDITIONER_ON) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_ON = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if self.fuel_quantity >= (self.fuel_consumption + Truck.AIR_CONDITIONER_ON) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Truck.AIR_CONDITIONER_ON) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


