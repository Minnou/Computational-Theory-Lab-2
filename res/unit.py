class Unit():
    __symbol = "0"
    __name = "unit_name"

    @property
    def name(self):
        return self.__name
    
    def to_string(self):
        return self.__symbol + " "