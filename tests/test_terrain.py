import pytest
from res.terrain.terrain import Terrain
from res.terrain.field import Field
from res.terrain.mountain import Mountain
from res.terrain.swamp import Swamp
from res.units.unit import Unit

def test_field_change_unit():
    t = Field()
    unit = Unit()
    t.change_unit(unit)
    assert unit.hp == unit.base_hp + t.hp_mod
    assert unit.hit == unit.base_hit + t.hit_mod

def test_mountain_change_unit():
    t = Mountain()
    unit = Unit()
    t.change_unit(unit)
    assert unit.hp == unit.base_hp + t.hp_mod
    assert unit.hit == unit.base_hit + t.hit_mod

def test_swamp_change_unit():
    t = Swamp()
    unit = Unit()
    t.change_unit(unit)
    assert unit.hp == unit.base_hp + t.hp_mod
    assert unit.hit == unit.base_hit + t.hit_mod

def test_field_change_unit_wrong_input():
    t = Field()
    unit = 'a'
    with pytest.raises(ValueError): 
        t.change_unit(unit)

def test_mountain_change_unit_wrong_input():
    t = Mountain()
    unit = 'a'
    with pytest.raises(ValueError): 
        t.change_unit(unit)

def test_swamp_change_unit_wrong_input():
    t = Swamp()
    unit = 'a'
    with pytest.raises(ValueError): 
        t.change_unit(unit)