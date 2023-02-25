from project_guild_system.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player_name: Player):
        if player_name.guild != "Unaffiliated" and player_name not in self.players:
            return f"Player {player_name.name} is in another guild."

        if player_name not in self.players:
            self.players.append(player_name)
            player_name.guild = self.name
            return f"Welcome player {player_name.name} to the guild {self.name}"

        return f"Player {player_name.name} is already in the guild."

    def kick_player(self, player_name: str):
        try:
            player_to_remove = [pl for pl in self.players if pl.name == player_name][0]
        except IndexError:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player_to_remove)
        player_to_remove.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join(pl.player_info() for pl in self.players)
        return f"Guild: {self.name}" + "\n" + players_info


guild = Guild("GGXrd")
player = Player("Pesho", 90, 90)
print(guild.assign_player(player))
print(guild.assign_player(player))
print(guild.kick_player("Gosho"))


