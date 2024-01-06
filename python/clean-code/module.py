import random
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll(self):
        return random.randint(1, self.sides)
    
d = Dice()
print("you rolled", d.roll())

# Better than class
print("you rolled", random.randint(1, 6))