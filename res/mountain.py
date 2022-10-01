from res.terrain import Terrain

class Mountain(Terrain):
    __symbol = "^"
    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "