from random import randint
from res.terrain import Terrain
from res.field import Field
from res.border import Border
from res.swamp import Swamp
from res.mountain import Mountain
from res.cursor import Cursor

class Board:
    __terrain = [[]] # слой объектов
    __units = [[]] # слой юнитов
    __var_terrain = [Swamp(), Mountain()] # варианты объектов
    __max_objects = [] # максимальное количество объектов
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
    
    #функция передвижения курсора по полю
    def move_cursor(self, x, y):
        if (x < self.width + 1 and x > 0 and y < self.height + 1 and y > 0):
            self.cursor.move(x,y)
    
    #Метод вывода поля на экран
    def display_board(self):
        board = ""
        for i in range(self.__height+2):
            for j in range(self.__width +2):
                if (self.__units[i][j] is None and (self.cursor.x !=j or self.cursor.y != i)):
                        board  = board + self.__terrain[i][j].to_string() 
                else:
                    if(not (self.__units[i][j] is None)):
                        board  = board + self.__units[i][j].to_string()
                    else:
                        board = board + self.cursor.to_string()
            board = board + "\n"
        print(board)