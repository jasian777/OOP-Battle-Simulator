import random

class Hacker:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(1, 1001)
        self.attack_power = random.randint(1, 1001)
        
    def battle_cry(self):
        return print("rawr click click")
        
    def attack(self):
        chance = random.randint(1, 10)
        if chance == 7:
            return random.randint(1, self.attack_power) + chance
        else:
            return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0