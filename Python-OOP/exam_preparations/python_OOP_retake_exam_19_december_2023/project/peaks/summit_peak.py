from project.peaks.base_peak import BasePeak
class SummitPeak(BasePeak):

    TYPE_ = "SummitPeak"

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        recomended_gear = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        return recomended_gear

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"