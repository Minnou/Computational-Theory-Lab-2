from res.unit_enum_factory import UnitFactory
import pickle

class Base():
    __symbol = "B" # символ базы на поле
    def __init__(self):
        self.__units = [] # список юнитов
        self.__max_unit_amount = 4 # максимальное количество юнитов в базе
    
    @property
    def max_unit_amount(self):
        return self.__max_unit_amount
    @property
    def unit_amount(self):
        return len(self.__units)

    def recruit_unit(self, unit):
        if (len(self.__units) < self.__max_unit_amount):
            self.__units.append(UnitFactory.CreateUnit(unit))

    def remove_unit(self):
        if(len(self.__units) > 0):
            return self.__units.pop()
    
    def print_base_units(self):
        if(len(self.__units) != 0):
            i = 1
            print("Гарнизон:\n" + str(len(self.__units)) + "/" + str(self.__max_unit_amount))
            for unit in self.__units:
                print(str(i) +". "+ unit.name)
                i = i + 1
        else:
            print("Гарнизон отсутствует")
    
    def to_string(self):
        return "\033[36m{}".format(self.__symbol) + " "
    
    def save_base(self):
        pickle.dump(self.__units, open("saves/base.pickle", "wb"))
    def load_base(self):
        units = pickle.load(open("saves/base.pickle", "rb"))  
        self.__units = units