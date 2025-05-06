# Верблюжья нотация
# WarriorHero
from tkinter.font import names


# Змеиная нотация
# warrior_hero

# Наследование

# Родительский|Супер класс
# class Hero:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def introduce(self):
#         return print(f"Я {self.name}, мой уровень {self.lvl}")
#
#     def action(self):
#         return print(f"{self.name} выполняет базовое действие!!")
#
#     def test(self):
#         pass
#
#
# hero = Hero("Hero", 100, 100)
#
#
# # Дочерний класс
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return print(f"Кастую огонь")
#
#     def action(self):
#         return print(f"{self.name} ничего не делает!!")
#
# mage_hero = MageHero("Маг", 100, 100, mp = 1000)
# mage_hero.action()


# class A:
#
#     def method_a(self):
#         return "A"
#
#
# class B(A):
#
#     def method_b(self):
#         return "B"
#
#
# class C(B):
#
#     def method_c(self):
#         return "C"
#
#
# test = C()
# print(test.)

class Animal:

    def action(self):
        return print("Animal action")


class Swim(Animal):

    def action(self):
        return print(f"Swim action")

class Fly(Animal):
    def action(self):
        super().action()
        # return print(f"Fly action")

# MRO(method resolution order)
class Duck(Fly, Swim):
    pass

donald_duck = Duck()

donald_duck.action()

# print(Duck.mro())