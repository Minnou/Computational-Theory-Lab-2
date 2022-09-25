from Terrain import Terrain

class Border(Terrain):
    __symbol = "X"
    def print(self):
        print("\033[37m{}".format(self.__symbol), end =' ')