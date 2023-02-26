from project_players_and_mosters.hero import Hero


class Wizard(Hero):
    def __init__(self, name: str, level: int):
        super().__init__(name, level)