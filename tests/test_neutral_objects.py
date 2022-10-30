import pytest
from res.objects.object import Object
from res.objects.log import Mighteous_Log
from res.objects.stone import Magic_Pebble
from res.objects.tree import Wise_Mythical_Tree
from res.units.unit import Unit

def test_log_change_unit():
    t = Mighteous_Log()
    unit = Unit()
    t.change_unit(unit)
    assert unit.hp == unit.base_hp + t.hp_mod
    assert unit.hit == unit.base_hit + t.hit_mod
    assert unit.mana == unit.base_hit + t.mana_mod

def test_mountain_change_unit():
    t = Magic_Pebble()
    unit = Unit()
    t.change_unit(unit)
    assert unit.hp == unit.base_hp + t.hp_mod
    assert unit.hit == unit.base_hit + t.hit_mod
    assert unit.mana == unit.base_hit + t.mana_mod

def test_tree_change_unit():
    t = Wise_Mythical_Tree()
    unit = Unit()
    t.change_unit(unit)
    assert unit.hp == unit.base_hp + t.hp_mod
    assert unit.hit == unit.base_hit + t.hit_mod
    assert unit.mana == unit.base_hit + t.mana_mod

def test_log_change_unit_wrong_input():
    t = Mighteous_Log()
    unit = 'a'
    with pytest.raises(ValueError): 
        t.change_unit(unit)

def test_stone_change_unit_wrong_input():
    t = Magic_Pebble()
    unit = 'a'
    with pytest.raises(ValueError): 
        t.change_unit(unit)

def test_tree_change_unit_wrong_input():
    t = Wise_Mythical_Tree()
    unit = 'a'
    with pytest.raises(ValueError): 
        t.change_unit(unit)