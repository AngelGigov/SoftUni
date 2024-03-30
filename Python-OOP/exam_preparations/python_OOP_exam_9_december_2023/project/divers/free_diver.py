from project.divers.base_diver import BaseDiver

class FreeDiver(BaseDiver):

    STARTING_OXY_LEVEL = 120
    OXY_DECREASE_INDEX = 0.6
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.STARTING_OXY_LEVEL)
    def miss(self, time_to_catch: int):
        if (self.oxygen_level - round(time_to_catch * self.OXY_DECREASE_INDEX)) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= round(time_to_catch * self.OXY_DECREASE_INDEX)


    def renew_oxy(self):
        self.oxygen_level = self.STARTING_OXY_LEVEL



