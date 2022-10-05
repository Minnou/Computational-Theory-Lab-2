from random import randint
from res.spearmen import Spearmen
from res.terrain import Terrain
from res.field import Field
from res.border import Border
from res.swamp import Swamp
from res.mountain import Mountain
from res.cursor import Cursor
from res.unit import Unit
from res.spearmen import Spearmen
from res.player_base import Base

class Board:
    __terrain = [[]] # слой объектов
    __units = [[]] # слой юнитов
    __var_terrain = [Swamp(), Mountain()] # варианты объектов
    __max_objects = [] # максимальное количество объектов
    __base = Base()
    #Конструктор класса
    def __init__(self, height, width, landscape, max_swamps, max_mountains):
        self.__height = height
        self.__width = width
        self.__landscape = landscape
        self.__max_objects.append(max_swamps)
        self.__max_objects.append(max_mountains)
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
        s = sum(self.__max_objects) #сумма максимальных количеств объектов
        for i in range(s):
            index = randint(0, len(self.__var_terrain) - 1) #Выбираем объект из доступных
            if((cur_objects[index] < self.__max_objects[index])): #Если позволяет максимальное количество, то ставим
                self.__terrain[randint(1,self.height)][randint(1,self.width)] = self.__var_terrain[index]
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
    
    def move_unit_left(self,unit):
        self._move_unit(unit,self.cursor.x - 1, self.cursor.y) 
    
    def move_unit_right(self,unit):
        self._move_unit(unit, self.cursor.x + 1, self.cursor.y)
    
    def move_unit_up(self,unit):
        self._move_unit(unit,self.cursor.x, self.cursor.y - 1)
    
    def move_unit_down(self,unit):
        self._move_unit(unit,self.cursor.x, self.cursor.y + 1)
    
    def base_show_units(self):
        self.__base.print()
    def base_recruit_unit(self):
        self.__base.recruit_unit()
    def base_unit_to_field(self):
        unit = self.__base.remove_unit()
        self.__units[1][2] = unit
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
            board = board + "Юнит " + self.__units[self.cursor.y][self.cursor.x].to_string() + "под курсором\n" 
        print(board)