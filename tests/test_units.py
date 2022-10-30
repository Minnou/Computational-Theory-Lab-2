import pytest
from res.units.unit import Unit
from res.units.archers import Archers
from res.units.infantry import Infantry
from res.units.mages import Mages
from res.units.bowman import Bowman
from res.units.crossbowman import Crossbowman
from res.units.healer import Healer
from res.units.knight import Knight
from res.units.spearmen import Spearmen
from res.units.wizard import Wizard

def test_check_bowman_interfaces():
    bowman = Bowman()
    assert isinstance(bowman, Archers)
    assert isinstance(bowman, Unit)
    assert not(isinstance(bowman, Infantry))
    assert not(isinstance(bowman, Mages))

def test_check_crossbowman_interfaces():
    crossbowman = Crossbowman()
    assert isinstance(crossbowman, Archers)
    assert isinstance(crossbowman, Unit)
    assert not(isinstance(crossbowman, Infantry))
    assert not(isinstance(crossbowman, Mages))

def test_check_healer_interfaces():
    healer = Healer()
    assert isinstance(healer, Mages)
    assert isinstance(healer, Unit)
    assert not(isinstance(healer, Infantry))
    assert not(isinstance(healer, Archers))

def test_check_knight_interfaces():
    knight = Knight()
    assert isinstance(knight, Infantry)
    assert isinstance(knight, Unit)
    assert not(isinstance(knight, Archers))
    assert not(isinstance(knight, Mages)) 

def test_check_spearmen_interfaces():
    spearmen = Spearmen()
    assert isinstance(spearmen, Infantry)
    assert isinstance(spearmen, Unit)
    assert not(isinstance(spearmen, Archers))
    assert not(isinstance(spearmen, Mages)) 

def test_check_wizard_interfaces():
    wizard = Wizard()
    assert isinstance(wizard, Mages)
    assert isinstance(wizard, Unit)
    assert not(isinstance(wizard, Infantry))
    assert not(isinstance(wizard, Archers))   

def test_unit_attributes_change():
    unit = Unit()
    hp = -10
    mana = 20
    hit = 8
    unit.change_unit(temp_hp= hp, temp_mana= mana, temp_hit= hit)
    assert unit.hp == unit.base_hp + hp
    assert unit.mana == unit.base_mana + mana
    assert unit.hit == unit.base_hit + hit


def test_unit_attributes_wrong_input():
    unit = Unit()
    hp = 'a'
    mana ='b'
    hit = 'c'
    with pytest.raises(ValueError): 
        unit.change_unit(temp_hp= hp, temp_mana= mana, temp_hit= hit)
    with pytest.raises(ValueError): 
        unit.change_unit(temp_mana= mana)
    with pytest.raises(ValueError): 
        unit.change_unit(temp_hit= hit)