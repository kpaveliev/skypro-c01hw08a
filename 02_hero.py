from math import log, ceil

class Hero:

    def __init__(self, name, experience=0):

        self.name = name
        self.experience = experience
        self.level = self.get_level()
        self.health = self.get_health()

    def add_experience(self, exp_):
        self.experience += exp_
        self.get_level()

    def get_level(self):
        if self.experience >= 15:
            self.level = int(log(self.experience / 15, 2)) + 2
        else:
            self.level = 1
        return self.level

    def get_health(self):
        self.health = 100
        for i in range(1, self.level):
            self.health = ceil(self.health * 0.15) * 10
        return self.health

    def __repr__(self):
        return f'Имя: {self.name}\n' + \
               f'Опыт: {self.experience}\n' + \
               f'Уровень: {self.level}\n' + \
               f'Здоровье: {self.health}\n'

# Testing
hero_1 = Hero('Hero1')
print(hero_1)

print()
hero_1.add_experience(10)
print(hero_1.experience)
print(hero_1.get_level())
print(hero_1.get_health())

print()
hero_1.add_experience(15)
print(hero_1.experience)
print(hero_1.get_level())
print(hero_1.get_health())

print()
hero_1.add_experience(15)
print(hero_1.experience)
print(hero_1.get_level())
print(hero_1.get_health())
