from Terrain import Terrain

class Swamp(Terrain):
    __symbol = "~"
    def print(self):
        print("\033[34m{}".format(self.__symbol), end =' ')