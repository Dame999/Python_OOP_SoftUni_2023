from abc import ABC, abstractmethod


class Appliance(ABC):
    def __init__(self, cost: float):
        self.cost = cost

    @abstractmethod
    def get_monthly_expense(self):
        pass
