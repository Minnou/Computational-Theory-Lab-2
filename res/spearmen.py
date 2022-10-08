from res.unit import Unit

class Spearmen(Unit):
    __symbol = "L"
    __name = "Копейщики"

    @property
    def name(self):
        return self.__name
        
    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "