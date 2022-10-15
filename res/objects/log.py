from res.objects.object import Object

class Mighteous_Log(Object):
    __symbol = "-"
    __name = "Мистическое Бревно Могущества"
    __temp_hit = 10

    @property
    def name(self):
        return self.__name

    def change_unit(self, unit):
        unit.change_unit(temp_hit = self.__temp_hit)

    def to_string(self):
        return "\033[35m{}".format(self.__symbol) + " "