class Teller:
    def __init__(self):
        self.shots = 1

    def ask(self, topic):
        if self.shots < 1:
            answer = "Ты исчерпал свои попытки, странник. Уходи!"

        else:
            if topic == "дорога":
                answer = "Отправляйся на север, держись самого края леса, " \
                         "найдешь пещеру, пройдешь внутри, от нее 2-3 лиги до городка"

            elif topic == "виверна":
                answer = "Победить виверну можно только магическим оружием. " \
                         "Спроси в городке сотрудников гильдии магического метода"

            elif topic == "дракон":
                answer = "За сломанной горой в скалах живет дракон." \
                         " С ним вообще никогда проблем не было"
            self.shots -= 1

        print(answer)


# Testing
if __name__ == '__main__':
    teller = Teller()
    teller.ask("дорога")
    teller.ask("виверна")
    teller.ask("дракон")
