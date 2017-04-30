#!/usr/bin/env python
# -- coding: UTF-8 --

class Player(object):
    def __init__(self, name, level=1, health=150, mana=100, strength=10, agility=12, intellect=8, stamina=15, critical=0, defense=10, speed=1):
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.stamina = stamina
        self.critical = critical
        self.defense = defense
        self.speed = speed
        self.inventory = []
        self.equipment = {
            1: None, # HEAD
            2: None, # SHOULDERS
            3: None, # CHEST
            4: None, # HANDS
            5: None, # LEGS
            6: None, # FEET
            7: None, # WEAPON
        }
        self.spellbook = []

    def __repr__(self):
        rep = "{\nName: " + self.name + "\n"
        rep += "Level: " + str(self.level) + "\n"
        rep += "Health: " + str(self.health) + "\n"
        rep += "Mana: " + str(self.mana) + "\n"
        rep += "Strength: " + str(self.strength) + "\n"
        rep += "Agility: " + str(self.agility) + "\n"
        rep += "Intellect: " + str(self.intellect) + "\n"
        rep += "Stamina: " + str(self.stamina) + "\n"
        rep += "Critical: " + str(self.critical) + "\n"
        rep += "Defense: " + str(self.defense) + "\n"
        rep += "Move speed: " + str(self.speed) + "\n"
        rep += "Inventory: {\n"
        for item in self.inventory:
            rep += "  " + item.__repr__() + "\n"
        rep += "  }\n"
        rep += "Equipment: {\n"
        for item in self.equipment:
            if self.equipment[item] != None:
                rep += "    " + self.equipment[item].__repr__() + "\n"
        rep += "  }\n"
        rep += "}"
        return rep

    def additem(self, item):
        if len(self.inventory) <= 20:
            self.inventory.append(item)
            return True
        else:
            print "Inventory is full"
            return False

    def equip(self, item):
        if item.type == 1: # Weapons
            if self.equipment[7] != None:
                if self.additem(self.equipment[7]):
                    self.equipment[7].remove_stats(self)
                    self.equipment[7] = item
                    item.add_stats(self)
                    self.inventory.remove(item)
            else:
                self.equipment[7] = item
                item.add_stats(self)
                self.inventory.remove(item)
        elif item.type == 2: # Armor
            if self.equipment[item.subtype] != None:
                if self.additem(self.equipment[item.subtype]):
                    self.equipment[item.subtype].remove_stats(self)
                    self.equipment[item.subtype] = self
                    item.add_stats(self)
                    self.inventory.remove(item)
            else:
                self.equipment[item.subtype] = item
                item.add_stats(self)
                self.inventory.remove(item)

    def use(self, item):
        if item in self.inventory:
            item.use(self)

    def cast(self, spell, target=None):
        if target == None: target = self;
        if spell in self.spellbook:
            spell.cast(target)

    def learn(self, spell):
        if spell not in self.spellbook:
            self.spellbook.append(spell)

    def unlearn(self, spell):
        if spell in self.spellbook:
            self.spellbook.remove(spell)
