class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f"{self.name} выполнил обычное действие")

    def attack(self):
        return print(f"{self.name} атакует")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision


    def attack(self):
        self.arrows -= 1
        if self.precision < 10:
            return print(f"{self.name} сделал неудачную атаку")
        else:
            return print(f"{self.name} сделал удачную атаку")


    def rest(self):
        self.arrows += 5
        return print(f"Стрелы пополнились")

    def status(self):
        return print(f"Имя: {self.name}, здоровье: {self.hp},"
                     f" количество стрел: {self.arrows}, точность: {self.precision}")


fighter = Archer("Боец", 100, 25, 7)

fighter.action()
fighter.attack()
fighter.rest()
fighter.status()