from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(25.5, 150.5)

    def test_if_initialization_is_correct(self):
        self.assertEqual(self.vehicle.fuel, 25.5)
        self.assertEqual(self.vehicle.horse_power, 150.5)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_vehicle_without_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as error:
            self.vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_vehicle_with_enough_fuel_then_subtract_from_total_fuel(self):
        self.vehicle.drive(5)
        self.assertEqual(self.vehicle.fuel, 19.25)

    def test_refuel_the_vehicle_with_more_fuel_than_needed_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(5)

        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel_the_vehicle_with_the_enough_fuel_adds_fuel_to_the_total_fuel_value(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 5)

    def test_str_method_returns_the_correct_information(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 150.5 " +
                         "horse power with 25.5 fuel left and 1.25 fuel consumption")


if __name__ == "__main__":
    main()
