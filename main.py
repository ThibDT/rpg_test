#!/usr/bin/env python
# -- coding: UTF-8 --

from item import *
from player import *
from spells import *

# Item(name, type, subtype, quality, min_attack, max_attack, defense, stat_type1, stat_value1, stat_type2, stat_value2, stat_type3, stat_value3)

player = Player("Player 1")
sword = Item("Sword test 1", 1, 1, 4, 150, 186, 0, 1, 47, 2, 62, 3, 39, 0)
sword2 = Item("Ultimate Sword of the Death", 1, 1, 5, 10438, 11765, 0, 1, 99999, 2, 99999,  3, 99999, 0)
healthPotion = Item("Health potion", 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, healingPotionSpell)

# ____________ God mod ______________

var = "player, sword, healthPotion"
command = raw_input("admin@game: $ ")
while command != "":
    exec command
    command = raw_input("admin@game: $ ")
