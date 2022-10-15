from res.units.archers import Archers

class Bowman(Archers):
    __symbol = "A"
    __name = "Лучники"

    __base_hp = 20
    __base_hit = 10
    __base_mana = 0

    hp = 20
    hit = 10
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