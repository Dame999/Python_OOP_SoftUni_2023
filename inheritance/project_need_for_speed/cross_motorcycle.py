from project_need_for_speed.family_car import FamilyCar
from project_need_for_speed.motorcycle import Motorcycle
from project_need_for_speed.vehicle import Vehicle


class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
