#!/usr/bin/env python
# -- coding: UTF-8 --

class Npc(object):

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
        
