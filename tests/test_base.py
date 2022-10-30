import pytest
from res.player_base import Base
from res.unit_enum_factory import Units

def test_unit_recruitment():
    b = Base()
    for i in range(b.max_unit_amount + 3):
        b.recruit_unit(Units(1))
    assert b.unit_amount <= b.max_unit_amount

def test_unit_rectuitment_wrong_input():
    b = Base()
    with pytest.raises(ValueError): 
        b.recruit_unit('a')

def test_unit_rectuitment_wrong_input2():
    b = Base()
    with pytest.raises(ValueError): 
        b.recruit_unit(Units(-999))

def test_remove_unit():
    b = Base()
    for i in range(b.max_unit_amount + 1):
        b.recruit_unit(Units(1))
    b.remove_unit()
    assert b.unit_amount == b.max_unit_amount - 1

def test_remove_unit2():
    b = Base()
    for i in range(b.max_unit_amount + 1):
        b.recruit_unit(Units(1))
    for i in range(b.max_unit_amount + 1):
        b.remove_unit()
    assert b.unit_amount == 0
