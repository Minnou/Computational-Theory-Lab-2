from random import randint
from res.terrain.border import Border
from res.terrain.swamp import Swamp
from res.terrain.mountain import Mountain
from res.objects.tree import Wise_Mythical_Tree
from res.objects.stone import Magic_Pebble
from res.objects.log import Mighteous_Log
from res.cursor import Cursor
from res.player_base import Base
from res.object_enum_factory import ObjectFactory
import pickle


class Board:
    __terrain = [[]] # слой объектов
    __units = [[]] # слой юнитов
    __var_terrain = [Swamp(), Mountain()] # варианты объектов ландшафта
    __var_neutral = [Wise_Mythical_Tree(), Magic_Pebble(), Mighteous_Log()] # варианты нейтральных объектов
    __max_terrain_objects = [] # максимальное количество объектов ландшафта
    __max_neutral_objects = [] # максимальное количество нейтральных объектов
    __base = Base()
    #Конструктор класса
    def __init__(self, height, width, landscape, max_swamps, max_mountains,max_tree,max_stone,max_log):
        self.__height = height
        self.__width = width
        self.__landscape = landscape
        self.__max_terrain_objects.append(max_swamps)
        self.__max_terrain_objects.append(max_mountains)
        self.__max_neutral_objects.append(max_tree)
        self.__max_neutral_objects.append(max_stone)
        self.__max_neutral_objects.append(max_log)
        self.cursor = Cursor(1,1) # создание курсора
    
    #Геттеры высоты и ширины поля
    @property
    def height(self):
        return self.__height
    @property
    def width(self):
        return self.__width
    
    #Метод генерации поля
    def generate_board(self):
        self.__terrain = [[Border()]* (self.width +2) for i in range(self.height + 2)]
        self.__units = [[None]* (self.width +2) for i in range(self.height + 2)]
        self.__units[1][1] = self.__base
        for i in range(1, self.__height+1):
            for j in range(1, self.__width+1):
                self.__terrain[i][j] = self.__landscape #по-умолчанию  клетка - объект ландшафта
        self.__randomize_objects()
    
    #Метод расстановки нейтральных объектов на поле
    def __randomize_objects(self):
        cur_objects = [0] * len(self.__var_terrain) #Счётчик объектов каждого типа
        s = sum(self.__max_terrain_objects) #сумма максимальных количеств объектов
        for i in range(s):
            index = randint(0, len(self.__var_terrain) - 1) #Выбираем объект из доступных
            if((cur_objects[index] < self.__max_terrain_objects[index])): #Если позволяет максимальное количество, то ставим
                self.__terrain[randint(1,self.height)][randint(1,self.width)] = self.__var_terrain[index]
                cur_objects[index] = cur_objects[index] + 1 #Увеличиваем счётчик
        cur_objects = [0] * len(self.__var_neutral) #Счётчик объектов каждого типа
        s = sum(self.__max_neutral_objects) #сумма максимальных количеств объектов
        for i in range(s):
            index = randint(0, len(self.__var_neutral) - 1) #Выбираем объект из доступных
            if((cur_objects[index] < self.__max_neutral_objects[index])): #Если позволяет максимальное количество, то ставим
                self.__terrain[randint(1,self.height)][randint(1,self.width)] = self.__var_neutral[index]
                cur_objects[index] = cur_objects[index] + 1 #Увеличиваем счётчик
    
    #Методы передвижения курсора по полю
    def _move_cursor(self, x, y):
        if (x < self.width + 1 and x > 0 and y < self.height + 1 and y > 0):
            self.cursor.move(x,y)
    
    def move_cursor_left(self):
        self._move_cursor(self.cursor.x - 1, self.cursor.y) 

    def move_cursor_right(self):
        self._move_cursor(self.cursor.x + 1, self.cursor.y)

    def move_cursor_up(self):
        self._move_cursor(self.cursor.x, self.cursor.y - 1)

    def move_cursor_down(self):
        self._move_cursor(self.cursor.x, self.cursor.y + 1)

    #Метод возвращающий юнит под курсором или нулл, если юнита нет
    def get_unit(self):
        if not(self.__units[self.cursor.y][self.cursor.x] is None):
            return self.__units[self.cursor.y][self.cursor.x]
        return None
    
    #Методы передвижения юнита
    def _move_unit(self, unit, x, y):
        if (x < self.width + 1 and x > 0 and y < self.height + 1 and y > 0 and self.__units[y][x] is None):
            self.__units[y][x] = unit
            self.__units[self.cursor.y][self.cursor.x] = None
            self._move_cursor(x,y)
            self.__terrain[y][x].change_unit(unit)
    
    def move_unit_left(self,unit):
        self._move_unit(unit,self.cursor.x - 1, self.cursor.y) 
    
    def move_unit_right(self,unit):
        self._move_unit(unit, self.cursor.x + 1, self.cursor.y)
    
    def move_unit_up(self,unit):
        self._move_unit(unit,self.cursor.x, self.cursor.y - 1)
    
    def move_unit_down(self,unit):
        self._move_unit(unit,self.cursor.x, self.cursor.y + 1)
    
    def base_show_units(self):
        self.__base.print_base_units()
    def base_recruit_unit(self,unit):
        self.__base.recruit_unit(unit)
    def base_unit_to_field(self):
        if (self.__units[1][2] is None or self.__units[2][2] is None or self.__units[2][1] is None):
            unit = self.__base.remove_unit()
            if self.__units[1][2] is None:
                self.__units[1][2] = unit
            elif self.__units[2][1] is None:
                self.__units[2][1] = unit
            elif self.__units[2][2] is None:
                self.__units[2][2] = unit
    
    #Метод вывода поля на экран
    def display_board(self):
        board = ""
        for i in range(self.__height+2):
            for j in range(self.__width +2):
                if (self.__units[i][j] is None and (self.cursor.x !=j or self.cursor.y != i)):
                        board  = board + self.__terrain[i][j].to_string() 
                else:
                    if(not (self.__units[i][j] is None) and (self.cursor.x !=j or self.cursor.y != i)):
                        board  = board + self.__units[i][j].to_string()
                    else:
                        board = board + self.cursor.to_string()
            board = board + "\n"
        if not(self.__units[self.cursor.y][self.cursor.x] is None) and not(isinstance(self.__units[self.cursor.y][self.cursor.x], Base)):
            unit = self.__units[self.cursor.y][self.cursor.x]
            board = board + "Юнит " + unit.name + " под курсором\n"
            board = board + unit.info_to_str() 
        print(board)
    
    #методы сохранения и загрузки игррового поля
    def save_board(self):
        pickle.dump(self, open("saves/board.pickle", "wb"))
        self.__base.save_base()
    @staticmethod
    def load_board():
        board = pickle.load(open("saves/board.pickle", "rb"))
        board.__base.load_base()
        return board
    
    def place_terrain_object(self, object):
        self.__terrain[self.cursor.y][self.cursor.x] = ObjectFactory.CreateObject(object)
