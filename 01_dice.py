#
import random

# Class
class Dice():

    def __init__(self, edges):
        self.edges = edges
        self.history = []

    def dice_throw(self):
        number = random.randrange(1, self.edges+1)
        self.history.append(str(number))
        return number

    def get_history(self, last_throws=2):
        len_ = len(self.history)
        return ', '.join(self.history[len_-last_throws:])


# Testing
if __name__ == '__main__':
    dice_4 = Dice(4)

    print(dice_4.dice_throw())
    print(dice_4.dice_throw())
    print(dice_4.dice_throw())
    print(dice_4.dice_throw())

    print(dice_4.get_history(4))
