from res.units.infantry import Infantry

class Knight(Infantry):
    __symbol = "K"
    __name = "Рыцари"

    __base_hp = 40
    __base_hit = 10
    __base_mana = 0
    
    def __init__(self):
        self.hp = 40
        self.hit = 10
        self.mana = 0

    #геттеры для параметров юнита
    @property
    def name(self):
        return self.__name
    @property
    def base_hp(self):
        return self.__base_hp
    @property
    def base_hit(self):
        return self.__base_hit
    @property
    def base_mana(self):
        return self.__base_mana

    def change_unit(self, temp_hp = 0, temp_hit = 0, temp_mana = 0):
        if not(isinstance(temp_hp, int)):
            raise ValueError('Здоровье должно быть числом!')
        if not(isinstance(temp_hit, int)):
            raise ValueError('Атака должна быть числом!')
        if not(isinstance(temp_mana, int)):
            raise ValueError('Мана должна быть числом!')
        self.hp = self.__base_hp + temp_hp
        self.hit = self.__base_hit + temp_hit
        self.mana = self.__base_mana + temp_mana
    
    def info_to_str(self):
        return "hp: " + str(self.hp) + " hit: " + str(self.hit) + " mana: " + str(self.mana)
    
    def to_string(self):
        return "\033[37m{}".format(self.__symbol) + " "