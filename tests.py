class Hero():

    def __init__(self, name):

        self.name = name

    def add_level(self, lvl):

        self.level += lvl

    def add_something(cls):


hero_1 = Hero('Hero1')
hero_1.add_level(2)

levels = {
    1: {'experience': 15, 'health': 100},
    2: {'experience': 30, 'health': 150},
    3: {'experience': 60, 'health': 230},
    4: {'experience': 120, 'health': 350},
    5: {'experience': 240, 'health': 530},
    6: {'experience': 480, 'health': 800},
    7: {'experience': 960, 'health': 1_200}
}

print(levels.1)

