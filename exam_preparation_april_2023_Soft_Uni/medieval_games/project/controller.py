from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    def add_player(self, *args: Player):
        added_names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_names.append(player.name)

        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    @staticmethod
    def add_stamina_to_player(player: Player, supply: Supply):
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

    def sustenance_the_player(self, player: Player, sustenance_type: str):

        for i in range(len(self.supplies) - 1, 0, -1):

            if self.supplies[i].__class__.__name__ == sustenance_type:
                supply = self.supplies.pop(i)
                self.add_stamina_to_player(player, supply)
                return f"{player.name} sustained successfully with {supply.name}."
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = [p for p in self.players if p.name == player_name][0]

            if player.stamina == 100:
                return f"{player_name} have enough stamina."

            if sustenance_type == "Food" or sustenance_type == "Drink":
                return self.sustenance_the_player(player, sustenance_type)

        except IndexError:
            pass

    @staticmethod
    def check_for_players_stamina(first_player: Player, second_player: Player):
        player_not_enough_stamina_message = []

        if first_player.stamina == 0:
            player_not_enough_stamina_message.append(f"Player {first_player.name} does not have enough stamina.")

        if second_player.stamina == 0:
            player_not_enough_stamina_message.append(f"Player {second_player.name} does not have enough stamina.")

        return '\n'.join(player_not_enough_stamina_message)

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        if first_player.stamina == 0 or second_player.stamina == 0:
            return self.check_for_players_stamina(first_player, second_player)

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        for _ in range(2):
            if second_player.stamina - first_player.stamina / 2 <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"

            second_player.stamina -= first_player.stamina / 2
            first_player, second_player = second_player, first_player
        else:
            if first_player.stamina > second_player.stamina:
                winner = first_player.name
            else:
                winner = second_player.name

            return f"Winner: {winner}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(player.__str__())

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)
