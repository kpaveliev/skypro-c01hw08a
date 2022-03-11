from math import ceil

health = 100
level = 1

for i in range(1, level):
    print(i)
    print(ceil(health * 0.15) * 10)
    health = ceil(health * 0.15) * 10

print(health)
