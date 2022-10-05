from res.unit import Unit
from res.spearmen import Spearmen
class Base():

    __units = []
    __symbol = "B"
    def recruit_unit(self):
        self.__units.append(Spearmen())

    def remove_unit(self):
        return self.__units.pop()
    
    def print(self):
        print(self.__units)
    
    def to_string(self):
        return "\033[36m{}".format(self.__symbol) + " "
    