class Customer:
    ID_NUMBER = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

        self.ID_NUMBER += 1

    @staticmethod
    def get_next_id():
        return Customer.ID_NUMBER

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
