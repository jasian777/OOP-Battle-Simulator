import random
class Hero:
    
    def __init__(self, name):
        self.name = name
        self.health = random.randint(100, 151)
        self.attack_power = random.randint(10, 26)
        
    def attack(self):
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0

    
