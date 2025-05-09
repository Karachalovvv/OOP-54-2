# Инкапсуляция

# import random
#
# class BankAccount:
#
#     def __init__(self, user, balance, password):
#         self.user = user # Открытый
#         self._balance = balance # Защищённый атрибут
#         self.__password = password # Приватный атрибут
#
#
#     def get_password(self):
#         return self.__password
#
#     def __generate_pass(self):
#         random.randint(1, 100)
#
#
#     def reset_pass(self):
#         self.password = self.__generate_pass()
#
# john = BankAccount("John", 1000, "123321")

# print(john.get_password())
# print(john.reset_pass())
# print(john._BankAccount__password)
# print(dir(john))


# Абстракция

from abc import ABC, abstractmethod

# Абстрактный класс
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#
#     def make_sound(self):
#         return print(f"{self.name} гав-гав")
#
#     def move(self):
#         return print(f"{self.name} move")
#
#
# tuzik = Dog("Tuzik")
#
# print(tuzik.name)

class SmsSend(ABC):

    @abstractmethod
    def send_otp_code(self):
        """

        Вам нужно будет реализовать логику отправки смс для вашей страны
        :return: смс
        """
        pass


class KGSmsSend(SmsSend):

    def send_otp_code(self):
        pass