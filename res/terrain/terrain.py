from res.units.unit import Unit

class Terrain:
    __symbol = "" #Символ ландшафта на поле
    __temp_hp = 0 #Изменение здоровья юнита
    __temp_hit =0 #Изменение атаки юнита

    @property
    def hp_mod(self):
        return self.__temp_hp
    
    @property
    def hit_mod(self):
        return self.__temp_hit
    
    def change_unit(self, unit):
        if not(isinstance(unit, Unit)):
            raise ValueError("Юнит должен пренадлежать классу Unit")
        unit.change_unit(self.__temp_hp, self.__temp_hit)
    def to_string(self):
        return self.__symbol + " "