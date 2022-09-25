from Terrain import Terrain

class Field(Terrain):
    __symbol = "*"
    def print(self):
        print("\033[32m{}".format(self.__symbol), end =' ')


