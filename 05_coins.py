class Hero:

    def __init__(self):
        self.coins = []

    def get_money(self):
        gold = 0
        conversion = {'gold': 1,
                      'silver': 10,
                      'bronze': 100}

        for coin in self.coins:
            gold += coin.value / conversion[coin.metal]

        print(gold)


class Coin:

    def __init__(self, value, metal):
        self.metal = metal
        self.value = value


# Testing
if __name__ == '__main__':
    hero = Hero()
    coins = [Coin(5, "gold"), Coin(30, "silver"), Coin(15, "bronze"), Coin(8, "gold")]
    hero.coins = coins
    hero.get_money()

