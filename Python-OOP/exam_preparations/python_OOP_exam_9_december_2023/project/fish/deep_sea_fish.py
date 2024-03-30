from project.fish.base_fish import BaseFish
class DeepSeaFish(BaseFish):

    TYPE_ = 'DeepSeaFish'
    
    def __init__(self, name, points):
        super().__init__(name, points, 180)
    def fish_details(self):
        return f"{self.TYPE_}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"

