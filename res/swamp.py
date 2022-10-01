from res.terrain import Terrain

class Swamp(Terrain):
    __symbol = "~"
    def to_string(self):
        return "\033[34m{}".format(self.__symbol) + " "