from project_players_and_mosters.dark_knight import DarkKnight
from project_players_and_mosters.elf import Elf
from project_players_and_mosters.hero import Hero


class BladeKnight(DarkKnight):
    def __init__(self, name: str, level: int):
        super().__init__(name, level)


