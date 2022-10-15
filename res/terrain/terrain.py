class Terrain:
    __symbol = "" #Символ ландшафта на поле
    __temp_hp = 0 #Изменение здоровья юнита
    __temp_hit =0 #Изменение атаки юнита

    def change_unit(self, unit):
        unit.change_unit(self.__temp_hp, self.__temp_hit)
    def to_string(self):
        return self.__symbol + " "