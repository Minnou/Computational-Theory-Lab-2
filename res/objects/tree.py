from res.objects.object import Object

class Wise_Mythical_Tree(Object):
    __symbol = "|"
    __name = "Мудрое Колдунское Древо"
    __temp_mana = 10

    @property
    def name(self):
        return self.__name

    def change_unit(self, unit):
         unit.change_unit(temp_mana = self.__temp_mana)

    def to_string(self):
        return "\033[35m{}".format(self.__symbol) + " "