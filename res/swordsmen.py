from res.unit import Unit

class Swordsmen(Unit):
    __symbol = "S"
    __name = "Мечники"
    
    @property
    def name(self):
        return self.__name

    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "