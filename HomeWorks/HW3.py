import random

class Student:

    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade


    def set_grade(self):
        self.__grade = random.randint(0, 100)


    def get_grade(self):
        return print(f"Оценка: {self.__grade}")


    def get_info(self):
        return print(f"Имя: {self.__name}, оценка: {self.__grade}")


chyngyz = Student("Chyngyz", 100)


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return print(f"Площадь круга: {3.14 * self.radius * self.radius}")


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return print(f"Площадь квадрата: {self.side * self.side}")