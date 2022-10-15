from res.objects.object import Object

class Magic_Pebble(Object):
    __symbol = "."
    __name = "Мистическая галька"
    __temp_hp = 10

    @property
    def name(self):
        return self.__name

    def change_unit(self, unit):
         unit.change_unit(temp_hp = self.__temp_hp)

    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "