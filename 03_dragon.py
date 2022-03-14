from math import log


class Dragon:

    def __init__(self, color, health):
        self.color = color
        self.health = health
        self.is_alive = True

    def get_health(self):
        print(f'Текущее здоровье: {self.health}')

    def bite(self, damage=10):
        if self.health > 0:
            self.health += damage
            print(f'Кусь на {damage}')
        else:
            print(f'Кусь невозможен, дракон мертв')

    def get_damage(self, damage):

        # in case damage is a degree of 2
        # health equals to closest degree of 2
        if log(damage, 2) % 1 == 0.0:
            self.health = 2 ** round(log(self.health, 2))
            print(f'Промах: {damage}, здоровье восстановлено')

        # in case self.health <= 0 dragon is dead
        elif (self.health - damage) <= 0:
            print(f'Получен урон: {self.health}, дракон умер')
            self.health = 0
            self.is_alive = False

        else:
            self.health -= damage
            print(f'Получен урон: {damage}')


# Testing
if __name__ == '__main__':
    dragon = Dragon('black', 500)
    dragon.get_health()

    dragon.get_damage(260)
    dragon.get_health()

    dragon.get_damage(4)
    dragon.get_health()

    dragon.bite()
    dragon.get_health()

    dragon.get_damage(266)
    dragon.bite()
    dragon.get_health()
