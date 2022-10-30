from res.objects.object import Object
from res.units.unit import Unit

class Wise_Mythical_Tree(Object):
    __symbol = "|"
    __name = "Мудрое Колдунское Древо"
    __temp_mana = 10
    __temp_hp = 0
    __temp_hit = 0
    #Геттеры параметров
    @property
    def name(self):
        return self.__name
    
    @property
    def hp_mod(self):
        return self.__temp_hp
    
    @property
    def hit_mod(self):
        return self.__temp_hit
    
    @property
    def mana_mod(self):
        return self.__temp_mana

    def change_unit(self, unit):
        if not(isinstance(unit, Unit)):
            raise ValueError("Юнит должен пренадлежать классу Unit")
        unit.change_unit(temp_hp = self.__temp_hp, temp_mana = self.__temp_mana, temp_hit = self.__temp_hit)

    def to_string(self):
        return "\033[35m{}".format(self.__symbol) + " "