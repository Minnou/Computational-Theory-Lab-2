from random import randint
from Terrain import Terrain
from Field import Field
from Border import Border
from Swamp import Swamp
from Mountain import Mountain

class Board:
    __terrain = [[]] # слой объектов
    __units = [[]] # слой юнитов
    __var_terrain = [Swamp(), Mountain()] # варианты объектов
    __max_objects = [] # максимальное количество объектов
    __object_chance = 20 # процентный шанс генерации какого-либо объекта
    #Конструктор класса
    def __init__(self, height, width, max_swamps, max_mountains):
        self.__height = height
        self.__width = width
        self.__max_objects.append(max_swamps)
        self.__max_objects.append(max_mountains)
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
        cur_objects = [0] * len(self.__var_terrain) #Счётчик объектов каждого типа
        for i in range(1, self.__height+1):
            for j in range(1, self.__width+1):
                self.__terrain[i][j] = Field() #по-умолчанию  клетка - чистое поле
                if(randint(0,100) < self.__object_chance): #Если не сгенерится объект, конечно же
                    index = randint(0, len(self.__var_terrain) - 1) #Выбираем объект из доступных
                    if((cur_objects[index] <= self.__max_objects[index])): #Если позволяет максимальное количество, то ставим
                        self.__terrain[i][j] = self.__var_terrain[index]
                        cur_objects[index] = cur_objects[index] + 1 #Увеличиваем счётчик
    #Метод вывода поля на экран
    def display_board(self):
        for i in range(self.__height+2):
            for j in range(self.__width +2):
                if (self.__units[i][j] == None):
                        self.__terrain[i][j].print() 
                else:
                    print(self.__units[i][j], end = '') 
            print("\n",end = '')
    
board = Board(10, 10,10, 7)
board.generate_board()
board.display_board()