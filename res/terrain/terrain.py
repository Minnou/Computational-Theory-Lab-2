class Terrain:
    __symbol = ""
    __temp_hp = 0
    __temp_hit =0

    def change_unit(self, unit):
        unit.hp = unit.__base_hp + self.__temp_hp
        unit.hp = unit.__base_hit + self.__temp_hit
    def to_string(self):
        return self.__symbol + " "