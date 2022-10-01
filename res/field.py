from res.terrain import Terrain

class Field(Terrain):
    __symbol = "*"
    def to_string(self):
        return "\033[32m{}".format(self.__symbol) + " "


