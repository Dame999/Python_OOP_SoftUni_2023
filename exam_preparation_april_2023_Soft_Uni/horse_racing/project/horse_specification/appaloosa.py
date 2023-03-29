from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def maximum_speed(self):
        return 120

    def train(self):
        if self.speed + 2 > self.maximum_speed():
            self.speed = self.maximum_speed()
        else:
            self.speed += 2

