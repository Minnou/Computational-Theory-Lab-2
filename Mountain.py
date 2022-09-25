from Terrain import Terrain

class Mountain(Terrain):
    __symbol = "^"
    def print(self):
        print("\033[37m{}".format(self.__symbol), end =' ')