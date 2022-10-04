from time import sleep
from res.board import Board
from res.field import Field
from res.field import Field
import keyboard

def clear_console():
    print("\033[H\033[J", end="")

def unit_control(unit):
    while (True):
        clear_console()
        board.display_board()
        print("q - отмена")
        key = keyboard.read_key()
        if (key == "q"):
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

board = Board(20, 20,Field(),10, 7)
board.generate_board()
board.display_board()
while (True):
    key = keyboard.read_key()
    print("\033[H\033[J", end="")   
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
    elif key == "enter":
        sleep(0.1)
        unit = board.get_unit()
        if not(unit is None):
            clear_console()
            board.display_board()
            print("w - движение\ns - способность")
            key = keyboard.read_key()
            # Событие - нажатие клавиши "w", берём контроль над юнитом
            if key == "w":
                sleep(0.1)
                unit_control(unit)
            clear_console()
    sleep(0.1)
    board.display_board()
