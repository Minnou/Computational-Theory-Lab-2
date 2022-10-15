class Object():
    __symbol = ""
    __name = "object_name"

    @property
    def name(self):
        return self.__name

    def to_string(self):
        return self.__symbol + " "