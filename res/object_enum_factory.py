from enum import Enum
from res.terrain.field import Field
from res.terrain.mountain import Mountain
from res.terrain.swamp import Swamp
from res.objects.log import Mighteous_Log
from res.objects.stone import Magic_Pebble
from res.objects.tree import Wise_Mythical_Tree

class Objects(Enum):
    Поле = 1
    Гора = 2
    Болото = 3
    Мистическая_галька = 4
    Мистическое_Бревно_Могущества = 5
    Мудрое_Колдунское_Древо = 6
    
class ObjectFactory():
    @staticmethod
    def CreateObject(object):
        if (object == Objects.Поле):
            return Field()
        if (object == Objects.Гора):
            return Mountain()
        if (object == Objects.Болото):
            return Swamp()
        if (object == Objects.Мистическая_галька):
            return Magic_Pebble()
        if (object == Objects.Мистическое_Бревно_Могущества):
            return Mighteous_Log()
        if (object == Objects.Мудрое_Колдунское_Древо):
            return Wise_Mythical_Tree()