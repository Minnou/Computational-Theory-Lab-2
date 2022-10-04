from res.unit import Unit

class Spearmen(Unit):
    __symbol = "S"
    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "