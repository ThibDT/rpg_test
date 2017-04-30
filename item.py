#!/usr/bin/env python
# -- coding: UTF-8 --

from datas import *
from player import Player
from spells import *

class Item(object):
    def __init__(self, name, itemType, subtype, quality, min_attack, max_attack, defense, stat_type1, stat_value1, stat_type2, stat_value2, stat_type3, stat_value3, spell):
        self.name = name
        self.type = itemType
        self.subtype = subtype
        self.quality = quality
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.defense = defense
        self.stat_type1 = stat_type1
        self.stat_value1 = stat_value1
        self.stat_type2 = stat_type2
        self.stat_value2 = stat_value2
        self.stat_type3 = stat_type3
        self.stat_value3 = stat_value3
        self.spell = spell

    def __repr__(self):
        rep = "{\n" + "Name: " + self.name + ",\n"
        rep += "Type: " + item_types[self.type] + ",\n"
        rep += "Subtype: " + item_subtypes[self.type][self.subtype] + ",\n"
        rep += "Quality: " + qualities[self.quality] + ",\n"
        if self.min_attack != 0 and self.max_attack != 0:
            rep += "Attack: " + str((self.min_attack  +  self.max_attack) / 2) + ",\n"
        if self.defense != 0:
            rep += "Defense: " + str(self.defense) + ",\n"
        if self.stat_type1 != 0:
            rep  += stat_types[self.stat_type1] + ": " + str(self.stat_value1) + "\n"
        if self.stat_type2 != 0:
            rep  += stat_types[self.stat_type2] + ": " + str(self.stat_value2) + "\n"
        if self.stat_type3 != 0:
            rep  += stat_types[self.stat_type3] + ": " + str(self.stat_value3) + "\n"
        rep  += "}"
        if self.spell != 0:
            rep += "Spell: " + self.spell.name + "\n"
        return rep

    def use(self, target):
        if self.type == 1: # Weapons & ARMOR
            target.equip(self)
            print self.name + " equiped."
        elif self.type == 2: # Armor
            target.equip(self)
            print self.name + " equiped."
        elif self.type == 3: # Consumable
            self.spell.cast(target)
            target.inventory.remove(self)
            print self.name + " used."
        else:
            print "Can't use " + self.name

    def add_stats(self, target):
        exec "target."+stat_types[self.stat_type1].lower()+" += "+str(self.stat_value1)
        exec "target."+stat_types[self.stat_type2].lower()+" += "+str(self.stat_value2)
        exec "target."+stat_types[self.stat_type3].lower()+" += "+str(self.stat_value3)

    def remove_stats(self, target):
        exec "target."+stat_types[self.stat_type1].lower()+" -= "+str(self.stat_value1)
        exec "target."+stat_types[self.stat_type2].lower()+" -= "+str(self.stat_value2)
        exec "target."+stat_types[self.stat_type3].lower()+" -= "+str(self.stat_value3)
