# from project.player import Player
#
# class Guild:
#     def __init__(self, name):
#         self.name = name
#         self.players = []
#
#     def assign_player(self, player: Player):
#         if player in self.players and player.guild == self.name:
#             return f"Player {player.name} is already in the guild."
#         elif player.guild != self.name and player.guild != "Unaffiliated":
#             return f"Player {player.name} is in another guild."
#         else:
#             self.players.append(player)
#             player.guild = self.name
#             return f"Welcome player {player.name} to the guild {self.name}"
#
#     def kick_player(self, player_name: str):
#         if player_name not in self.players:
#             return f"Player {player_name} is not in the guild."
#         elif player_name in self.players and player.guild == self.name:
#             self.players.pop(player_name)
#             player.guild = "Unaffiliated"
#             return f"Player {player_name} has been removed from the guild."
#
#     def guild_info(self):
#         players_info = '\n'.join([player.player_info() for player in self.players])
#         return f'Guild: {self.name}\n{players_info}'
#
from project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players and player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = '\n'.join([player.player_info() for player in self.players])
        return f'Guild: {self.name}\n{players_info}'