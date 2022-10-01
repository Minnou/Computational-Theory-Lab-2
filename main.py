from time import sleep
from res.board import Board
from res.field import Field
from res.field import Field
import keyboard

board = Board(10, 10,Field(),10, 7)
board.generate_board()
board.display_board()
while (True):
    key = keyboard.read_key()
    print("\033[H\033[J", end="")   
    if (key == "esc"):
        break
    # Событие - нажатие клавиши "4", курсор двигается влево
    elif key == "4":
        board.move_cursor(board.cursor.x - 1, board.cursor.y) 
    # Событие - нажатие клавиши "6", курсор двигается вправо 
    elif key == "6":
        board.move_cursor(board.cursor.x + 1, board.cursor.y)
    # Событие - нажатие клавиши "8", курсор двигается вверх 
    elif key == "8":
        board.move_cursor(board.cursor.x, board.cursor.y - 1)
    # Событие - нажатие клавиши "2", курсор двигается вниз
    elif key == "2":
        board.move_cursor(board.cursor.x, board.cursor.y + 1)
    elif key == "enter":
        pass
    sleep(0.1)
    board.display_board()
