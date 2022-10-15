from res.terrain.terrain import Terrain

class Swamp(Terrain):
    __symbol = "~"
    __temp_hp = -10
    __temp_hit = 0

    def change_unit(self, unit):
        unit.change_unit(self.__temp_hp, self.__temp_hit)
    
    def to_string(self):
        return "\033[34m{}".format(self.__symbol) + " "