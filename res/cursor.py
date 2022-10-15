class Cursor():
    __symbol = "X" # символ курсора
    #конструктор
    def __init__(self,x,y):
        self.__x = x #координаты x
        self.__y = y #и y
    
    #геттеры и сеттеры для координат курсора
    @property    
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
            
    @property    
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
    
    #Метод передвижения курсора по заданным координатам
    def move(self, x ,y):
        self.x = x
        self.y = y
    
    def to_string(self):
        return "\033[31m{}".format(self.__symbol) + " "