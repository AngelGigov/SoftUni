from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type != "KneePad" and equipment_type != "ElbowPad":
            raise Exception("Invalid equipment type!")
        equipment = KneePad() if "KneePad" else ElbowPad()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."



    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type != "OutdoorTeam" and team_type != "IndoorTeam":
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."
        team = OutdoorTeam(team_name, country, advantage) if team_type == "OutdoorTeam" else IndoorTeam(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."




    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = [e for e in self.equipment if e.TYPE == equipment_type][-1]
        team = next(filter(lambda t: t.name == team_name, self.teams))
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."
    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([eq.increase_price() for eq in self.equipment if eq.TYPE == equipment_type])
        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)

        if team1.TYPE_ != team2.TYPE_:
            raise Exception("Game cannot start! Team types mismatch!")

        team_one_points = team1.advantage + sum(e.protection for e in team1.equipment)
        team_two_points = team2.advantage + sum(e.protection for e in team2.equipment)

        if team_one_points > team_two_points:
            team1.win()
            return f"The winner is {team_name1}."
        elif team_one_points < team_two_points:
            team2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
        Number of Teams: {len(self.teams)}
        Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)


#helping method
    def _find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())



