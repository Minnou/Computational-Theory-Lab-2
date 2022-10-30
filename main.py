from time import sleep
from res.board import Board
from res.terrain.field import Field
from res.units.unit import Unit
import keyboard
from res.unit_enum_factory import Units
from res.player_base import Base
from res.object_enum_factory import Objects

#Управление в игре осуществляется цифрами 8 4 6 2 на нумпаде
#И клавишей энтер

#Ввод параметра размера игрового поля
def size_param():
    a = (int)(input())
    if a <= 3:
        print("Число должно быть больше трёх")
        size_param()
    else:
        return a
#Ввод параметра максимального количества объектов опред. вида
def ter_param(width,height):
    z = (int)(input())
    if z > width*height/4:
        print("Число должно быть меньше " + (str)(width*height/4))
        ter_param(width,height)
    if z <= 0:
        print("Число должно быть больше 0")
        ter_param(width,height)
    return z
#Ввод всех параметров поля и его генерация
def generate():
    print("Желаете загрузить поле?[y/n]")
    answer = input()
    if(answer == "y" or answer == "yes"):
        return Board.load_board()
    print("Введите размер поля по горизонтали")
    width = size_param()
    print("Введите размер поля по вертикали")
    height = size_param()
    print("Введите количество болот")
    swamp = ter_param(width,height)
    print("Введите количество гор")
    mountains = ter_param(width,height)
    print("Введите количество деревьев")
    tree = ter_param(width,height)
    print("Введите количество камней")
    stone = ter_param(width,height)
    print("Введите количество брёвен")
    log = ter_param(width,height)
    board = Board(height,width,Field(),swamp,mountains,tree,stone,log)
    board.generate_board()
    return board

board = generate()
board.display_board()
#Функция очистки консоли
def clear_console():
    print("\033[H\033[J", end="")
#Функция управления юнитом
def unit_control(unit):
    while (True):
        clear_console()
        board.display_board()
        print("q - отмена")
        key = keyboard.read_key()
        if (key == "q" or key == "й"):
            break
        # Событие - нажатие клавиши "4", курсор и юнит двигается влево
        elif key == "4":
            board.move_unit_left(unit)
        # Событие - нажатие клавиши "6", курсор и юнит двигается вправо 
        elif key == "6":
            board.move_unit_right(unit)
        # Событие - нажатие клавиши "8", курсор и юнит двигается вверх 
        elif key == "8":
            board.move_unit_up(unit)
        # Событие - нажатие клавиши "2", курсор и юнит двигается вниз
        elif key == "2":
            board.move_unit_down(unit)
        sleep(0.1)
#Функция управления базой
def base_control():
    while(True):
                clear_console()
                print("w - вывести юнит на поле\nr - нанять юнит\nq - отмена")
                board.base_show_units()
                board.display_board()
                key = keyboard.read_key()
                # Событие - нажатие клавиши "w" выводит юнит на поле
                if key == "w" or key == "ц":
                    sleep(0.1)
                    board.base_unit_to_field()
                #Найм юнита
                elif key == "r" or key == "к":
                    sleep(0.2)
                    #Вывод всех юнитов из перечисления юнитов
                    for possible_unit in Units:
                        print(str(possible_unit.value) + ". " + possible_unit.name)
                    key = keyboard.read_key()
                    sleep(0.1)
                    if(key.isdigit()):  
                        if len(Units._member_names_) >= int(key) and int(key) > 0:  
                            board.base_recruit_unit(Units(int(key)))
                elif key == "q" or key =="й":
                    sleep(0.1)
                    break
#Функция редактирования поля
#(можно менять ландшафт и объекты)
def place_objects():
    while (True):
        key = keyboard.read_key() 
        if (key == "esc"):
            sleep(0.2)
            break
        # Событие - нажатие клавиши "4", курсор двигается влево
        elif key == "4":
            board.move_cursor_left()
        # Событие - нажатие клавиши "6", курсор двигается вправо 
        elif key == "6":
            board.move_cursor_right()
        # Событие - нажатие клавиши "8", курсор двигается вверх 
        elif key == "8":
            board.move_cursor_up()
        # Событие - нажатие клавиши "2", курсор двигается вниз
        elif key == "2":
            board.move_cursor_down()
        #Редактирование поля 
        elif key == "enter":
            sleep(0.1)
            #Вывод всех объектов из перечисления объектов
            for pos_object in Objects:
                print(str(pos_object.value) + ". " + pos_object.name)
            key = keyboard.read_key()
            sleep(0.1)
            if(key.isdigit()):  
                if len(Objects._member_names_) >= int(key) and int(key) > 0:  
                    board.place_terrain_object(Objects(int(key)))
        clear_console()
        sleep(0.1)
        board.display_board()
        print("esc - закончить расстановку")

place_objects()
clear_console()
board.display_board()
#Основной игровой цикл
while (True):
    key = keyboard.read_key() 
    if (key == "esc"):
        break
    # Событие - нажатие клавиши "4", курсор двигается влево
    elif key == "4":
        board.move_cursor_left()
    # Событие - нажатие клавиши "6", курсор двигается вправо 
    elif key == "6":
        board.move_cursor_right()
    # Событие - нажатие клавиши "8", курсор двигается вверх 
    elif key == "8":
        board.move_cursor_up()
    # Событие - нажатие клавиши "2", курсор двигается вниз
    elif key == "2":
        board.move_cursor_down()
    #Энтер выбирает либо юнит под курсором либо базу под курсором
    elif key == "enter":
        sleep(0.1)
        unit = board.get_unit()
        if (isinstance(unit, Unit)):
            clear_console()
            board.display_board()
            print("w - движение")
            key = keyboard.read_key()
            # Событие - нажатие клавиши "w", берём контроль над юнитом
            if key == "w" or key == "ц":
                sleep(0.1)
                unit_control(unit)
        elif(isinstance(unit, Base)):
            base_control()
    #Сохранение и загрузка поля
    elif key == "m" or key == "ь":
        Board.save_board(board)
    elif key == "o" or key == "щ":
        board = Board.load_board()
    clear_console()
    sleep(0.1)
    board.display_board()
    print("m - сохранить поле\no - загрузить поле\nesc - закончить игру")
