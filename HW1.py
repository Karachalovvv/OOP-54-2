class Person:
    def __init__(self, name = "Имя", age = "Возраст", city = "Город"):
        self.name_1 = name
        self.age_1 = age
        self.city_1 = city

    def introduce(self):
        print(f'\\\"Привет, меня зовут {self.name_1}, мой age {self.age_1}, мой city {self.city_1}\\\"')

    def is_adult(self):
        print(self.age_1 >= 18)



chyngyz = Person("Чынгыз", 16, "Бишкек")

chyngyz.introduce()

beksultan = Person("Бексултан", 18, "Бишкек")
sultan = Person("Султан", 20, "Бишкек")

chyngyz.is_adult()
beksultan.is_adult()
sultan.is_adult()