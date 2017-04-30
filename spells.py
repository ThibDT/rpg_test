class Spell(object):
    def __init__(self, name, description, cooldown, cost=0, heal=0, damage=0, manaboost=0):
        self.name = name
        self.description = description
        self.cooldown = cooldown
        self.cost = cost
        self.heal = heal
        self.damage = damage
        self.manaboost = manaboost

    def cast(self, target):
        target.health += self.heal
        target.health -= self.damage
        target.mana += self.manaboost


healingPotionSpell = Spell("Healing Potion", "Restore 50 hp.", 15, 0, 50, 0, 0)
manaPotionSpell = Spell("Mana Potion", "Restore 35 mp.", 15, 0, 0, 0, 35)
