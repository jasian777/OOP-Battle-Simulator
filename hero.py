class Hero:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        
    def attack(self):
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0

    pass
