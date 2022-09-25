from random import randint
from Terrain import Terrain
from Field import Field
from Border import Border
from Swamp import Swamp
from Mountain import Mountain

class Board:
    __terrain = [[]]
    __units = [[]]
    __var_terrain = [Swamp(), Field(), Mountain()]
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    @property
    def height(self):
        return self.__height
    @property
    def width(self):
        return self.__width
    def generate_board(self):
        self.__terrain = [[Border()]* (self.width +2) for i in range(self.height + 2)]
        self.__units = [[None]* (self.width +2) for i in range(self.height + 2)]
        for i in range(1, self.__height+1):
            for j in range(1, self.__width+1):
                self.__terrain[i][j] = self.__var_terrain[randint(0, len(self.__var_terrain) - 1)]
    def display_board(self):
        for i in range(self.__height+2):
            for j in range(self.__width +2):
                if (self.__units[i][j] == None):
                        self.__terrain[i][j].print() 
                else:
                    print(self.__units[i][j], end = '') 
            print("\n",end = '')
    
board = Board(10, 10)
board.generate_board()
board.display_board()