from res.unit import Unit

class Cavalry(Unit):
    __symbol = "C"
    __name = "Кавалерия"
    
    @property
    def name(self):
        return self.__name

    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "