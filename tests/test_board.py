import pytest
from res.terrain import field
from res import board

def test_size():
    b = board.Board(15,20, field.Field(),1,1,1,1,1)
    assert b.width == 20
    assert b.height == 15

def test_height_wrong_number():
    with pytest.raises(ValueError): 
        b = board.Board(3,15, field.Field(),1,1,1,1,1)
def test_width_wrong_number():
    with pytest.raises(ValueError): 
        b = board.Board(15,3, field.Field(),1,1,1,1,1)

def test_wrong_input_height():
    with pytest.raises(ValueError): 
        b = board.Board('a',15, field.Field(),1,1,1,1,1)

def test_wrong_input_width():
    with pytest.raises(ValueError): 
        b = board.Board(15,'b', field.Field(),1,1,1,1,1)

def test_wrong_input_landscape():
    with pytest.raises(ValueError): 
        b = board.Board(15,15, 15,1,1,1,1,1)

def test_wrong_input_max_num1():
    with pytest.raises(ValueError): 
        b = board.Board(15,15, field.Field(),'a',1,1,1,1)

def test_wrong_input_max_num2():
    with pytest.raises(ValueError): 
        b = board.Board(15,15, field.Field(),1,'a',1,1,1)

def test_wrong_input_max_num3():
    with pytest.raises(ValueError): 
        b = board.Board(15,15, field.Field(),1,1,'a',1,1)

def test_wrong_input_max_num4():
    with pytest.raises(ValueError): 
        b = board.Board(15,15, field.Field(),1,1,1,'a',1)

def test_wrong_input_max_num5():
    with pytest.raises(ValueError): 
        b = board.Board(15,15, field.Field(),1,1,1,1,'a') 