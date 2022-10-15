from res.units.archers import Archers

class Crossbowman(Archers):
    __symbol = "C"
    __name = "Арбалетчики"

    __base_hp = 30
    __base_hit = 20
    __base_mana = 0

    hp = 30
    hit = 20
    mana = 0

    @property
    def name(self):
        return self.__name

    def change_unit(self, temp_hp = 0, temp_hit = 0, temp_mana = 0):
        self.hp = self.__base_hp + temp_hp
        self.hit = self.__base_hit + temp_hit
        self.mana = self.__base_mana + temp_mana

    def info_to_str(self):
        return "hp: " + str(self.hp) + " hit: " + str(self.hit) + " mana: " + str(self.mana)

    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "