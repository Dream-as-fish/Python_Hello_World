import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        print(random.randint(1, self.sides))


dice = Die()
for i in range(10):
    dice.roll()

print("_______________________________________________________________")

dice.sides = 10
for i in range(10):
    dice.roll()

print("_______________________________________________________________")

dice.sides = 20
for i in range(10):
    dice.roll()