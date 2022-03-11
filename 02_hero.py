
class Hero():

    def __init__(self, name, health=100, experience=0, level=1):

        self.name = name
        self.health = health
        self.experience = experience
        self.level = level

    def add_experience(self, exp_):

        levels = {
            1: {'experience': 15, 'health': 100},
            2: {'experience': 30, 'health': 150},
            3: {'experience': 60, 'health': 230},
            4: {'experience': 120, 'health': 350},
            5: {'experience': 240, 'health': 530},
            6: {'experience': 480, 'health': 800},
            7: {'experience': 960, 'health': 1_200}
        }

        self.experience += exp_

        for key, values in levels.items():
            if exp_ in range(values['experience']):
                self.level = key
                self.health = values['health']
                break

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health


hero_1 = Hero('Hero1')

hero_1.add_experience(10)
print(hero_1.experience)
print(hero_1.get_level())
print(hero_1.get_health())


hero_1.add_experience(15)
print(hero_1.experience)
print(hero_1.get_level())
print(hero_1.get_health())


hero_1.add_experience(50)
print(hero_1.experience)
print(hero_1.get_level())
print(hero_1.get_health())