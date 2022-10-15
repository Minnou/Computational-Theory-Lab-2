from res.terrain.terrain import Terrain

class Field(Terrain):
    __symbol = "*"
    __temp_hp = 0
    __temp_hit = 0

    def change_unit(self, unit):
        unit.change_unit(self.__temp_hp, self.__temp_hit)
    
    def to_string(self):
        return "\033[32m{}".format(self.__symbol) + " "


