from typing import List

from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber
from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
class SummitQuestManagerApp:

    CLIMBERS_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAKS_TYPES = {'ArcticPeak': ArcticPeak, 'SummitPeak': SummitPeak}
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBERS_TYPES.keys():
            return f"{climber_type} doesn't exist in our register."

        elif self._get_climber_by_name(climber_name):
            return f"{climber_name} has been already registered."
        else:
            self.climbers.append(self.CLIMBERS_TYPES[climber_type](climber_name))
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAKS_TYPES.keys():
            return f"{peak_type} is an unknown type of peak."
        peak = self.PEAKS_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = self._get_climber_by_name(climber_name)
        peak = self._get_peak_by_name(peak_name)
        needed_gear = peak.get_recommended_gear()
        missing_gear = set(needed_gear) - set(gear)
        if set(needed_gear).issubset(set(gear)):
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        #Climber Validation
        climber = self._get_climber_by_name(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        #Peak Validation
        peak = self._get_peak_by_name(peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        #Climb check
        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)


    #Helping Method
    def _get_climber_by_name(self, climber_name: str):
        climber = [c for c in self.climbers if c.name == climber_name]
        return climber[0] if climber else None

    def _get_peak_by_name(self, peak_name: str):
        peak = [p for p in self.peaks if p.name == peak_name]
        return peak[0] if peak else None


