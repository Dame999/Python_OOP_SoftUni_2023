from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if not MovieWorld.customer_capacity() == len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if not MovieWorld.dvd_capacity() == len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if customer_id == c.id][0]
        dvd = [d for d in self.dvds if dvd_id == d.id][0]

        try:
            dvd = [d for d in customer.rented_dvds if dvd_id == d.id][0]
            return f"{customer.name} has already rented {dvd.name}"

        except IndexError:

            try:
                dvd_rented = [d for d in self.dvds if d.is_rented][0]
                return "DVD is already rented"

            except IndexError:

                if customer.age < dvd.age_restriction:
                    return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

                customer.rented_dvds.append(dvd)
                dvd.is_rented = True
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if customer_id == c.id][0]
        dvd = [d for d in self.dvds if dvd_id == d.id][0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(str(customer))
        for dvd in self.dvds:
            result.append(str(dvd))
        return '\n'.join(result)