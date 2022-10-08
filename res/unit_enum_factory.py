from enum import Enum
from res.spearmen import Spearmen
from res.swordsmen import Swordsmen
from res.cavalry import Cavalry

class Units(Enum):
    Копейщики = 1
    Мечники = 2
    Кавалерия = 3

class UnitFactory():
    @staticmethod
    def CreateUnit(unit):
        if  (unit == Units.Копейщики):
            return Spearmen()
        if (unit == Units.Мечники):
            return Swordsmen()
        if (unit == Units.Кавалерия):
            return Cavalry()
