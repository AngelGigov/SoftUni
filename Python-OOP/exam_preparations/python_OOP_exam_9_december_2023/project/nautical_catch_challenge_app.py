from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES.keys():
            return f"{diver_type} is not allowed in our competition."

        diver = self._get_diver_name(diver_name)

        if diver is not None:
            return f"{diver_name} is already a participant."

        new_diver = self.DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES.keys():
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._get_fish_by_name(fish_name)

        if fish is not None:
            return f"{fish_name} is already permitted."

        new_fish = self.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        #Diver validation
        diver = self._get_diver_name(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        #Fish Validation
        fish = self._get_fish_by_name(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        #Health Check
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        #Oxygen Level Comparison
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f'{diver_name} hits a {fish.points}pt. {fish_name}.'


    def health_recovery(self):
        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.oxygen_level = diver.STARTING_OXY_LEVEL
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self._get_diver_name(diver_name)
        fish_details = [fish.fish_details() for fish in diver.catch]

        catch_report = "\n".join(fish_details)
        return f"**{diver_name} Catch Report**\n{catch_report}"

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(
            healthy_divers,
            key=lambda x: (-x.competition_points, -len(x.catch), x.name),
        )

        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_divers)
        return result


    #Helping Methods

    def _get_diver_name(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name]
        return diver[0] if diver else None

    def _get_fish_by_name(self, fish_name: str):
        fish = [f for f in self.fish_list if f.name == fish_name]
        return fish[0] if fish else None

nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())
