import random

class Die:
    def __init__(self, name):
        self.name = name
        self.sides = int(name[1:])  # Converts "d20" to 20

    def roll(self):
        return random.randint(1, self.sides)
    
    def __repr__(self):
        return f"{self.name} (d{self.sides})"
