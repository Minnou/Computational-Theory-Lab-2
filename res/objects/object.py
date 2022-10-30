from res.units.unit import Unit

class Object():
    __symbol = "" #символ объекта на поле
    __name = "object_name" #имя объекта
    __temp_hp = 0 #Изменение здоровья юнита
    __temp_mana = 0 #Изменение маны юнита
    __temp_hit = 0 #Изменениеатаки юнита
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
        return self.__symbol + " "